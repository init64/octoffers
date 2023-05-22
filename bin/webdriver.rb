require "selenium-webdriver"

service = Selenium::WebDriver::Service.chrome(path: '/usr/bin/chromedriver')
options = Selenium::WebDriver::Chrome::Options.new
options.add_argument("--headless")
$driver = Selenium::WebDriver.for :chrome, service: service, options: options
$wait = Selenium::WebDriver::Wait.new(timeout: 120)
