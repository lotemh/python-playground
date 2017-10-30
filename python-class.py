
class Person:
    # class_variable
    life_expectancy = 90
    country_code_dict = {1: "India", 3: "France", 62: "Mozambique"}

    def __init__(self, country):
        self.country = country

    def print_country(self):
        print("person is from {0}".format(self.country))

    @classmethod
    def print_life_expectancy(cls):
        # cls is an object that holds class itself, not an instance of the class
        print("life expectancy: {0}".format(cls.life_expectancy))

    @classmethod
    def from_country_code(cls, country_code):
        # cls is an object that holds class itself, not an instance of the class
        # in this case classmethod is used as constructor overloading
        country = cls.country_code_dict[country_code]
        return cls(country)


if __name__ == "__main__":
    print("life expectancy: {0}".format(Person.life_expectancy))
    Person.print_life_expectancy()  # the same
    Person.from_country_code(62).print_country()
