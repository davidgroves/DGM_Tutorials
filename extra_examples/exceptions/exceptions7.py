# If you want useful error messages, you should pass in a message.
# This is an example that will crash with your custom exception in something
# more like a real world situation.

class UserDoesntExist(Exception):
    pass

def usernameLookup(username):
    if username == "Alice":
        print(f"Yes, {username} exists")
    else:
        raise UserDoesntExist(f"{username} doesn't exist")

usernameLookup("Alice")
usernameLookup("Bob")

print("I crashed before I got here !")
