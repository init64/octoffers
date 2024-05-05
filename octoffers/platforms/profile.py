from pathlib import Path
from shutil import rmtree
from os import mkdir
from platforms.driver import Driver

class Profile:
    def __init__(self, name: str = "default"):
        self.name = name
        self.workdir = Path.home().joinpath(".config/octoffers/profiles")

    def delete(self, *profile_names: list):
        for name in profile_names:
            rmtree(self.workdir.joinpath(name), ignore_errors=1)

    def create(self, profile_name: str):
        profile_name = self.name if not profile_name else profile_name
        Driver()._initiate_driver("--headless", f"--user-data-dir={self.workdir.joinpath(profile_name)}")

    def list(self):
        for profile in self.workdir.iterdir():
            if profile.is_dir():
                print(profile.name)

