from fire import Fire
from platforms.djinni import Djinni


class Octoffers:
    def __init__(self):
        self.djinni_driver = Djinni()

    def fetch_all_jobs_by_role(
        self,
        role: str,
        tools=None,
        min_salary=None,
        exclusion_words=None,
    ):
        url = f"https://{self.djinni_driver.driver_instance.domain}/jobs/"
        self.djinni_driver.fetch_jobs(url, role, tools, min_salary, exclusion_words)

    def fetch_all_jobs_for_me(
        self,
        tools=["dbt", "aws", "python", "pandas"],
        min_salary=None,
        exclusion_words=["Junior", "platform", "Hydrographic"],
    ):
        url = f"https://{self.djinni_driver.driver_instance.domain}/jobs/my/"
        self.djinni_driver.fetch_jobs(url, tools, min_salary, exclusion_words)

    def apply_jobs(self):
        self.djinni_driver.apply_jobs()

    def manual_authorization(self):
        self.djinni_driver.manual_authorization()


Fire(Octoffers)
