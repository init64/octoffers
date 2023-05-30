require_relative "driver"

class Djinni < Driver 
  JOB_FILTER = "?all-keywords=&any-of-keywords=&exclude-keywords="

  def fetch_jobs(role="devops")
    10.times do |idx|
      $driver.navigate.to("https://#{@domain}/jobs/#{JOB_FILTER}&primary_keyword=#{role}&page=#{idx}")
      opportunity_elements = $wait.until {
        $driver.find_elements(css: '.profile')
      } 
      opportunity_elements.each do |element|
        puts "#{element.text}\n   |- #{element.attribute("href")}"
        $db.execute(
          "INSERT INTO jobs(role, link, category) VALUES(?, ?, ?)",
          [element.text, element.attribute("href"), role]
        )
      end
    end
  end

  def apply_jobs(role="devops", msg_template)
    job_links = $db.execute("SELECT link, role, id FROM jobs WHERE category = '#{role}'")
    # puts "#{job_links}"
    job_links.each do |opportunity|
      puts "[ #{opportunity[1]} ]".ljust(80) + " Checking..." 
      $driver.navigate.to(opportunity[0])
      begin
        $wait.until { $driver.find_element(:xpath, "//*[contains(text(), 'This job doesn')]") }
        puts "  |-[ This job dosen't match ]"
      rescue
        puts "  |-[ Acceptable ]" 
      end

      button = nil
      begin
        button = $wait.until { $driver.find_element(:xpath, "//*[contains(text(), 'Apply')]") } 
      rescue
        puts "  |-[ Already checked ]"
        $db.execute <<-SQL
          UPDATE jobs
          SET checked = #{true}
          WHERE id = #{opportunity[2]}
        SQL
        next
      end

      button.click
      template = $wait.until { $driver.find_element(:xpath, "//*[contains(text(), '#{msg_template}')]") }  
      template.click
      apply_buttons = $wait.until { $driver.find_elements(:tag_name, "button") }  
      begin
        apply_buttons.each do |button|
          if button.text == "Apply for the job" || button.text == "Share contacts and start talking"
            puts "[ #{opportunity[1]} ]".ljust(80) + " Applying..." 
            $driver.execute_script('arguments[0].scrollIntoView(true);', button)
            button.click
            next
          end
        end
      rescue  
        puts "!! STALE ERROR D: !!"
      end
    end

  end

  def manual_authorization()
    $driver.get("https://#{@domain}/login")
    puts $driver.current_url
    btn = $wait.until { 
      $driver.find_element(xpath: "//*[@value='github']") 
    }
    btn.click
    $wait.until { $driver.current_url == "https://#{@domain}" } 
  end

end
