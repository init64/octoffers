from fire import Fire
from platforms.djinni import Djinni


class Octoffers:
    def __init__(self):
        self.djinni = Djinni()

    def manual_authorization(self):
        self.djinni.manual_authorization()


Fire(Octoffers)
