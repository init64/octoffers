from fire import Fire
from platforms.djinni import Djinni
from platforms.profile import Profile

class Octoffers:
    def __init__(self):
        self.djinni = Djinni()
        self.profile = Profile()
        try:
            from platforms.private.indeed import Indeed
            self.indeed = Indeed()

        except ModuleNotFoundError:
            print("Private drivers weren't found")

    def manual_authorization(self):
        self.djinni.manual_authorization()

Fire(Octoffers)
