# In this program, we use a try/except clause to catch and handle the exception.

capitals = {
    "England": "London",
    "France": "Paris",
    "Germany": "Berlin"
}

for nation in ["England", "France", "Germany", "Italy"]:
    try:
        print (f"The capital of {nation} is {capitals[nation]}")
    except KeyError:
        print (f"I don't know the capital of {nation}, sorry !")
