import re

class Person:
    def __init__(self,name,family): #, national_id):
        self.name = name
        self.family = family
        # self._national_id = national_id


    # 1
    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and re.match("^[A-Z]+$", name,re.I):
            self._name = name
        else:
            raise ValueError("نام نامعتبر است")

    name = property(get_name, set_name)


    # 2
    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        self._family = family

    #
    # # Read Only
    # @property
    # def national_id(self):
    #     return self._national_id

#
#
#
# person = Person("ali","alipour", "1234")
# print(person.__dict__)
# person.name = "alireza"
# person.national_id = "4567"
# print(person.__dict__)
