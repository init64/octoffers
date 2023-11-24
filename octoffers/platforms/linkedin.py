from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time, os
from urllib.parse import urlencode

from dotenv import load_dotenv

load_dotenv()


class LinkedInDriver:
    selenium_driver = None

    def __init__(self, token, chromium_path):
        if chromium_path == "" or token == "":
            raise Exception("check envs")

        options = Options()
        options.binary_location = chromium_path
        options.add_experimental_option("detach", True)
        # options.add_argument(
        # r"--user-data-dir=//Users/hararudoka/dev/selenium-linkedin/profile"
        # )
        self.selenium_driver = webdriver.Chrome(options=options)

        # Go to the LinkedIn home page
        self.selenium_driver.get("https://www.linkedin.com")

        # Set the cookie
        self.selenium_driver.add_cookie(
            {
                "name": "li_at",
                "value": token,
            }
        )

        # Refresh the page to apply the cookie (optional)
        self.selenium_driver.refresh()

    def login(self, username, password):
        if self.selenium_driver == None:
            raise Exception("Selenium driver is not initialized")

        # Logging into LinkedIn
        self.selenium_driver.get("https://linkedin.com/uas/login")
        time.sleep(2)
        u = self.selenium_driver.find_element(By.ID, "username")
        u.send_keys(username)  # Enter Your Email Address
        p = self.selenium_driver.find_element(By.ID, "password")
        p.send_keys(password)  # Enter Your Password
        self.selenium_driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def search(self, params):
        if self.selenium_driver == None:
            raise Exception("Selenium driver is not initialized")

        ## job search

        # https://www.linkedin.com/jobs/search/?keywords=golang&location=London%20Area%2C%20United%20Kingdom

        # TODO: ensure that request parsed correctly

        url = f"https://www.linkedin.com/jobs/search/?{urlencode(params)}"

        self.selenium_driver.get(url)
        time.sleep(2)

        # search for jobs
        search = self.selenium_driver.find_element(
            By.XPATH, '//*[@id="main"]/div/div[1]/div/ul'
        )

        jobs = search.find_elements(By.TAG_NAME, "li")

        id_list = []
        for job in jobs:
            id = job.get_attribute("data-occludable-job-id")
            if id != None:
                id_list.append(int(id))

        for id in id_list:
            # https://www.linkedin.com/jobs/view/3765979648
            print(f"https://www.linkedin.com/jobs/view/{id}")

        return id_list


if __name__ == "__main__":
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    chromium_path = os.getenv("CHROMIUM_PATH")

    # 'li_at' cookie value
    token = os.getenv("TOKEN")

    driver = LinkedInDriver(token, chromium_path)
    # driver.login(username, password)
    # params = {
    #   "keywords": "golang",
    #   "location": "London Area, United Kingdom",
    # }
    # driver.search(params)
