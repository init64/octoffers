require "selenium-webdriver"
require "dotenv/load"

service = RUBY_PLATFORM.match("mingw") ?
	Selenium::WebDriver::Service.chrome :
	Selenium::WebDriver::Service.chrome.chrome(path: '/usr/bin/chromedriver') 
	
puts ENV["HEADLESS"]
options = ENV["HEADLESS"] == 1 ? Selenium::WebDriver::Chrome::Options.new : nil

if options
	options.add_argument("--headless")
end

$driver = Selenium::WebDriver.for :chrome, service: service, options: options
$wait = Selenium::WebDriver::Wait.new(timeout: 3)
