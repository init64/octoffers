import os
import sys
from dotenv import load_dotenv
import re
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# import sqlite3

from platforms.driver import Driver
from db.schemes.djinni import db
from intergrations.chat_gpt import get_cover_letter_from_openai

load_dotenv()


class Djinni:
    JOB_FILTER = "?all-keywords=&any-of-keywords=&exclude-keywords="

    def __init__(self, domain="djinni.co"):
        self.driver_instance = Driver(domain)
        self.wait = WebDriverWait(self.driver_instance.driver, 20)
        # db = DatabaseManager(db_path)

    def _get_job_list(self, url):
        self.driver_instance.driver.get(url)
        self.driver_instance.driver.save_screenshot(
            "screenshots/screenshot_vacancies.png"
        )
        return self.wait.until(
            lambda driver: driver.find_elements(
                By.CSS_SELECTOR,
                "ul.list-unstyled.list-jobs.mb-4 li.list-jobs__item.job-list__item",
            )
        )

    def _parse_salary(self, salary_text):
        # Extracting numeric values from a salary string
        numbers = [int(s) for s in re.findall(r"\b\d+\b", salary_text)]
        return min(numbers) if numbers else 0

    def fetch_jobs(
        self, url, role=None, tools=None, min_salary=None, exclusion_words=None
    ):
        for idx in range(1, 2):
            full_url = (
                f"{url}{self.JOB_FILTER}&primary_keyword={role}&page={idx}"
                if role
                else f"{url}&page={idx}"
            )
            print(full_url)

            job_list = self._get_job_list(full_url)

            for job_item in job_list:
                title_element = job_item.find_element(
                    By.CSS_SELECTOR,
                    "div.job-list-item__title.mb-1 a.job-list-item__link",
                )
                job_title = title_element.text
                job_link = title_element.get_attribute("href")
                job_id = job_link.split("/jobs/")[1].split("-")[0]

                description_element_id = "job-description-" + job_id
                description_html = job_item.find_element(
                    By.ID, description_element_id
                ).get_attribute("data-original-text")
                soup = BeautifulSoup(description_html, "lxml")
                job_description = soup.get_text(separator=" ", strip=True)

                # Retrieving salary information
                salary_element = job_item.find_elements(
                    By.CSS_SELECTOR, "span.public-salary-item"
                )
                salary_text = salary_element[0].text if salary_element else None
                salary = self._parse_salary(salary_text) if salary_text else 0

                # Checking tools, minimum wage and exception words
                matches = True  # By default, we assume that the vacancy is suitable

                print(
                    f"{job_title}\n   |- {job_id}\n   |- Salary: {salary}\n   |- {job_link}\n  |- Matches: {matches}"
                )

                if tools and not all(
                    tool.lower() in job_description.lower() for tool in tools
                ):
                    matches = False  # If no tools are found
                    print("Condition triggered tools")
                if min_salary and salary < min_salary:
                    matches = False  # If the salary is below the minimum
                    print("Condition triggered min_salary")
                if exclusion_words and any(
                    word.lower() in job_title.lower() for word in exclusion_words
                ):
                    matches = False  # If exception words are found
                    print("Condition triggered exclusion_words")

                job_exists = db.execute(
                    "SELECT 1 FROM jobs WHERE job_id = ?", (job_id,)
                ).fetchone()

                if not job_exists:
                    try:
                        db.execute(
                            "INSERT INTO jobs(job_id, role, link, category, source, description, salary, matches) VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
                            (
                                job_id,
                                job_title,
                                job_link,
                                "my_role",
                                "djinni",
                                job_description,
                                salary,
                                matches,
                            ),
                        )
                        db.commit()
                    except sqlite3.Error as e:
                        print(f"Data insertion error: {e}")

    def apply_jobs(self):
        # Retrieving all matching records from a database
        job_entries = db.execute(
            "SELECT job_id, role, link, category, source, description FROM jobs WHERE matches = 1 AND cv_sent = 0"
        ).fetchall()

        for job_entry in job_entries[:1]:
            job_id, role, job_link, category, source, job_description = job_entry
            print(f"{job_link:<80} Checking...")

            self.driver_instance.driver.get(job_link)

            # Search for the “Apply for a vacancy” button and click on it
            try:
                apply_button = self.wait.until(
                    lambda driver: driver.find_element(
                        By.CSS_SELECTOR,
                        "button.btn.btn-primary.js-inbox-toggle-reply-form",
                    )
                )
                # Take and save a screenshot
                self.driver_instance.driver.save_screenshot(
                    "screenshots/screenshot_send_cv.png"
                )
                apply_button.click()
            except TimeoutException:
                print("Button not found or already applied")
                self.driver_instance.driver.save_screenshot(
                    "screenshots/screenshot_send_cv.png"
                )
                continue

            # Generating a cover letter
            cover_letter = get_cover_letter_from_openai(job_description)

            # Inserting a Cover Letter and Submitting an Application
            try:
                message_box = self.wait.until(
                    lambda driver: driver.find_element(By.ID, "message")
                )
                message_box.send_keys(cover_letter)
                submit_button = self.wait.until(
                    lambda driver: driver.find_element(By.ID, "job_apply")
                )
                submit_button.click()
            except TimeoutException:
                print("Could not send application")
                continue

            # Updating the submission status in the database
            db.execute(
                "UPDATE jobs SET cv_sent = 1 WHERE job_id = ?", (job_id,)
            )
            db.commit()

            print(f"Application sent for {job_link}")
