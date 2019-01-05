# You can just make an error happen with the raise keyword.
# Remember unhandled, your program will crash.

# This can be useful though if you want a function to throw an exception some main code will handle.

def DatabaseLookup(username):
    # Imagine some code is here that gets an entry from a database.

    # if user exists
        # return user
    # else
        raise KeyError

try:
    user = DatabaseLookup(username="foo")
except KeyError:
    print("Something went wrong, we got a KeyError, our user doesn't exist!")
