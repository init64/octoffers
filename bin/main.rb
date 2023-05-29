# webgtx @ 2023 

require "thor"
require_relative "platforms/djinni"

class OctOffers < Thor
  def self.exit_on_faliure
    true
  end

  desc "fetch PLATFORM ROLE", "fetch all available jobs on the platform"
  def fetch(platform, role="DevOps")
    case platform
    when "djinni"
      if ENV["DJINNI_SESSIONID"] 
        DjinniDriver.session_authorization
        DjinniDriver.fetch_jobs(role)
      else
        puts "You didn't provide a COOKIE_SESSIONID into dotenv file"
      end
    else
      puts "Invalid platform"
    end
    # require_relative "platforms/#{platform}/#{script}.rb"
  end

  desc "clear", "Clear all fetched jobs"
  def clear()
    DjinniDriver.clear_jobs
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
