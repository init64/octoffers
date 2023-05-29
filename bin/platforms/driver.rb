require_relative "../../db/schema"
require_relative "../webdriver"
require "dotenv/load"

class Driver
  attr_reader :session_cookie, :domain

  def initialize(session_cookie, domain)
    @session_cookie = session_cookie
    @domain = domain
  end

  def session_authorization()
    $driver.get("https://#{@domain}")
    $driver.manage.add_cookie(@session_cookie)
  end

  # I'm use "self" only for now, in near future I'll use different
  # for many platforms
  def self.clear()
    $db.execute("DELETE FROM jobs;") 
  end

end
