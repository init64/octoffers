from fire import Fire
from platforms.djinni import Djinni

class Octoffers():
  def __init__(self):
    self.coverletter = "Hello, I'm looking for job"
  
  def djinni(self, apply: bool = False):
    driver = Djinni()
    return driver.apply(self.coverletter) if apply else "driver's under development"


Fire(Octoffers)
