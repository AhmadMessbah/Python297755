import re

from project.da.person_da import PersonDa
from project.model.person import Person
from project.tools.validation import Validation


class PersonController:   
    @classmethod
    def save(cls, name, family):
        try:
            if Validation.name_validation(name) and Validation.name_validation(family):
                person = Person(name, family)
                da = PersonDa()
                # check if name is not duplicate
                da.save(person)
                return True, "Person Saved"
            else:
                raise ValueError("Invalid Data")
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, name, family):
        try:
            if Validation.name_validation(name) and Validation.name_validation(family):
                person = Person(name, family)
                da = PersonDa()
                da.edit(person)
                return True, "Person Edited"
            else:
                raise ValueError("Invalid Data")
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, name, family):
        try:
            if Validation.name_validation(name) and Validation.name_validation(family):
                person = Person(name, family)
                da = PersonDa()
                da.remove(person)
                return True, "Person Remove"
            else:
                raise ValueError("Invalid Data")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            da = PersonDa()
            return True, da.find_all()
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_family(cls,family):
        try:
            da = PersonDa()
            return True, da.find_by_family(family)
        except Exception as e:
            return False, str(e)