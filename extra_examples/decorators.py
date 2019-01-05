
def start_and_stop(my_function):
    print(f"Starting to do {my_function.__name__}")
    my_function()
    print(f"Finished {my_function.__name__}")

@start_and_stop
def say_hello():
    print("Hello !")
    return None

say_hello()