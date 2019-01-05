# Python has some built in decorators.

# This is the property decorator
# You usually use it on methods in classes that don't require parameters.
# This way you can treat them as "computed variables" rather than as functions.

# See example below

class Person:
    def __init__(self, firstname, surname):
        self.firstname = firstname
        self.surname = surname

    @property
    def fullname(self):
        return f"{self.firstname} {self.surname}"

    @property
    def fullname_property(self):
        return f"{self.firstname} {self.surname}"


dave = Person("David", "Groves")
print(dave.fullname_property)
