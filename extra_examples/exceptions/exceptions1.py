# When Python would crash for some reason, it throws an exception.

# You can "catch" the exception and handle it, if crashing isn't the correct thing to do.

# Here is an example program which will crash, because you try and look up something in the dictionary
# which doesn't have a key

capitals = {
    "England": "London",
    "France": "Paris",
    "Germany": "Berlin"
}

for nation in ["England", "France", "Germany", "Italy"]:
    print (f"The capital of {nation} is {capitals[nation]}")

# When it crashes, you will see it prints "KeyError: Italy" as part of the traceback.
