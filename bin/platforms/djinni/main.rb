require_relative "../../webdriver" 
require "dotenv/load"

module DjinniDriver 
  DOMAIN = "djinni.co"
  JOB_FILTER = "?all-keywords=&any-of-keywords=&exclude-keywords=&primary_keyword=DevOps"
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

  def self.fetch_jobs()
    10.times do |idx|
      $driver.navigate.to("https://#{DOMAIN}/jobs/#{JOB_FILTER}&page=#{idx}")
      opportunity_elements = $wait.until {
        $driver.find_elements(css: '.profile')
      } 
      opportunity_elements.each do |element|
        puts "#{element.text}"
      end
    end
  end
end

