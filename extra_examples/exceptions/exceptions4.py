# Although you can do this, you really really shouldn't.

# You should always catch exceptions you expect to happen and to handle, not just anything.
# Then something can go wrong you didn't predict, and you will carry on regardless, often with
# bad side effects.

try:
    print("Hello !")
    # Lets not bother declaring b or c, lets just use them anyway !
    a = b * c
except:
    print("Something went wrong, who knows what !")