require_relative "driver"

class Djinni < Driver 
  DOMAIN = "djinni.co"
  JOB_FILTER = "?all-keywords=&any-of-keywords=&exclude-keywords="

  def fetch_jobs(role="devops")
    10.times do |idx|
      $driver.navigate.to("https://#{DOMAIN}/jobs/#{JOB_FILTER}&primary_keyword=#{role}&page=#{idx}")
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

  def manual_authorization()
    $driver.get("https://#{DOMAIN}/login")
    puts $driver.current_url
    btn = $wait.until { 
      $driver.find_element(xpath: "//*[@value='github']") 
    }
    btn.click
    $wait.until { $driver.current_url == "https://#{DOMAIN}" } 
  end

end
