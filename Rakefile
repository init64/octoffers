task default: :test

task :test do
  require_relative "bin/platforms/djinni"
  
  djinni_driver = Djinni.new(
    {
      name: "sessionid",
      value: ENV["DJINNI_SESSIONID"],
      domain: "djinni.co",
      path: "/",
      expires: (Time.now + 3600).to_i
    }, 
    "djinni.co"
  )
  djinni_driver.session_authorization
  djinni_driver.fetch_jobs
end

task :db do
  ruby "db/schema.rb"
end
