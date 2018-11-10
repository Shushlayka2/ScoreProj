import models.db as db

class Diploma_logic:

    def __init__(self, diploma):
        self.diploma = diploma

    def release(self):
        print(f"{self.diploma.thesis} released!")