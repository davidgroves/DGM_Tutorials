# This program won't crash, your custom exception is handled with a message being printed.


class UserDoesntExist(Exception):
    pass

def usernameLookup(username):
    if username == "Alice":
        print(f"Yes, {username} exists")
    else:
        raise UserDoesntExist(f"{username} doesn't exist")

for name in ["Alice", "Bob"]:
    try:
        usernameLookup(name)
    except UserDoesntExist:
        print(f"{name} doesn't exist !")

print("I didn't crash !")