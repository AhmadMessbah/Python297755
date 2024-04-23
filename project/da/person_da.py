class PersonDa:
    def save(self, person):
        print(person.name,person.family, "Saved to database")

    def edit(self, person):
        print(person.name, person.family, "Edited to database")

    def remove(self, person):
        print(person.name, person.family, "Removed to database")

    def find_all(self):
        print("FindAll")

    def find_by_family(self,family):
        print("FindAll")
