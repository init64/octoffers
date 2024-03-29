import os, sys, subprocess
sys.path.append(os.getcwd())
sys.path.append(os.path.join(os.getcwd(), "octoffers"))
from time import sleep
from icecream import ic
from multiprocessing import Process
try:
    from octoffers.platforms.private.indeed import Indeed
except:
    print("Private drivers weren't found")

class TestCaseDefault:
    def test_indeed_login(self):
        Indeed().login(os.environ["MOCK_EMAILADDR"])

    def test_indeed_fetch(self):
        Indeed().fetch(pages=10, role="python")

    def test_indeed_apply(self):
        Indeed().apply()
