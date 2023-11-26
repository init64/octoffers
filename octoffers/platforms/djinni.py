from os import environ


class Djinni:
    def __init__(self):
        try:
            self.authtoken = environ["DJINNI_TOKEN"]
        except KeyError:
            self.authtoken = "somerandomtoken9382"


    def apply(self, msg):
        print("Auhtorize client with TOKEN", self.authtoken)
        print("Send coverletter: ", msg)
