
from tigereye.api import ApiVIew

class MiscView(ApiVIew):

    def check(self):
        return "I'm OK"

    def error(self):
        1 / 0