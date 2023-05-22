# webgtx @ 2023 

require "thor"
require_relative "platforms/djinni/main"

class OctOffers < Thor
  def self.exit_on_faliure
    true
  end

  desc "start PLATFORM", "Start automated job on the platform"
  def start(platform)
    case platform
    when "djinni"
      if ENV["DJINNI_SESSIONID"] 
        DjinniDriver.session_authorization
        DjinniDriver.fetch_jobs
      else
        puts "You didn't provide a COOKIE_SESSIONID into dotenv file"
      end
    else
      puts "Invalid platform"
    end
    # require_relative "platforms/#{platform}/#{script}.rb"
  end
  
  desc "auth PLATFORM TYPE ?USERNAME ?PASSWORD", "Login into platform"
  def auth(platform, type = "oauth2", username = nil, password = nil)
    puts("Feature isn't ready yet", platform, type, username, password)  
  end
end

OctOffers.start
