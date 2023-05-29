# webgtx @ 2023 

require "thor"
require_relative "platforms/djinni"

class OctOffers < Thor
  def self.exit_on_faliure
    true
  end

  desc "fetch PLATFORM ROLE", "fetch all available jobs on the platform"
  def fetch(platform, role)
    case platform
    when "djinni"
      if ENV["DJINNI_SESSIONID"] 
        djinni_driver = Djinni.new(ENV["DJINNI_SESSIONID"])
        djinni_driver.session_authorization
        djinni_driver.fetch_jobs(role)
      else
        puts "You didn't provide a COOKIE_SESSIONID into dotenv file"
      end
    else
      puts "Invalid platform"
    end
  end

  desc "clear", "Clear all fetched jobs"
  def clear()
    Driver.clear
    puts "Done"
  end

  desc "show CATEGORY|ALL", "Show all fetched jobs"
  def show(category)
    res = $db.execute(
      category != "all" ? 
        "SELECT role, link, category FROM jobs WHERE category = '#{category}'" 
        : "SELECT * FROM jobs;" 
    )
    res.each do |dat|
      puts "[ #{dat[0]} ]\n    |- #{dat[1]}\n    |- #{dat[2]}" 
    end
  end
end

OctOffers.start
