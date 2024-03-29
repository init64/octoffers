import os
from pathlib import Path

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from os import getenv, environ

load_dotenv()

# Getting cookie values
session_id = getenv("DJINNI_SESSION_ID")

# Generating a list of cookies
session_cookies = [{"name": "sessionid", "value": session_id, "domain": ".djinni.co"}]


class Driver:
    def __init__(self, domain):
        self.domain = domain
        self.session_cookies = session_cookies
        self.octoffers_path = f"{Path.home()}/Octoffers" if os.name == "nt" else f"{environ['HOME']}/.config/octoffers"

    def _initiate_driver(self, *argv):
        chrome_options = Options()
        for arg in argv:
            chrome_options.add_argument(str(arg))
        self.driver = webdriver.Chrome(options=chrome_options)
        # self.driver.implicitly_wait(5)
        self.wait = WebDriverWait(self.driver, 5)

    def session_authorization(self):
        self.driver.get(f"https://{self.domain}")

        # Adding an explicit wait to ensure the page has loaded
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        for cookie in self.session_cookies:
            self.driver.add_cookie(cookie)

        # Reloading the page to apply cookies
        self.driver.refresh()
