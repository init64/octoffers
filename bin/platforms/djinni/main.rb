require_relative "../../webdriver" 
require_relative "../../../db/schema.rb"
require "dotenv/load"

module DjinniDriver 
  DOMAIN = "djinni.co"
  JOB_FILTER = "?all-keywords=&any-of-keywords=&exclude-keywords="
  SESSION_COOKIE =  {
    name: "sessionid",
    value: ENV["DJINNI_SESSIONID"],
    domain: DOMAIN,
    path: "/",
    expires: (Time.now + 3600).to_i
  } 

  def self.session_authorization()
    $driver.get("https://#{DOMAIN}")
    $driver.manage.add_cookie(SESSION_COOKIE)
  end

  def self.manual_authorization()
    $driver.get("https://djinni.co/login")
    puts $driver.current_url
    btn = $wait.until { 
      $driver.find_element(xpath: "//*[@value='github']") 
    }
    btn.click
    $wait.until { $driver.current_url == DOMAIN } 
  end

  def self.fetch_jobs(role)
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

  def self.clear_jobs()
    $db.execute("DELETE FROM jobs;")
  end
end
