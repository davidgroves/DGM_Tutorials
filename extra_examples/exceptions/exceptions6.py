# This is a custom exception class

# By convention, you have the word "Error" at the end of exception classes.
# They also inherit from the built in Exception class, which is why they have
# Exception in brackets in declaring the class. This might be "magic" for now
# and you will need to learn more about class exceptions later.

# The most basic custom exception doesn't actually need to do anything !

# This isn't actually very interesting though.

class UserDoesntExist(Exception):
    pass

raise UserDoesntExist
