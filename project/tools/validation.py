import re


class Validation:
    @classmethod
    def name_validation(cls, name):
        return bool(re.match("^[A-Za-z\s]{2,30}$", name))
