from fire import Fire
from octoffers.platforms.djinni import Djinni
from octoffers.platforms.profile import Profile

class Octoffers:
    def __init__(self, profile: str = None):
        self.djinni = Djinni()
        self.profile = Profile()
        try:
            from octoffers.platforms.private import Indeed
            self.indeed = Indeed(profile=profile)

        except ModuleNotFoundError:
            print("Private drivers weren't found")

    def manual_authorization(self):
        self.djinni.manual_authorization()

def main():
    Fire(Octoffers)

if __name__ == "__main__":
    main()