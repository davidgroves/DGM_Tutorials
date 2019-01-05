# Here is another example

for i in range(10, -10, -1):
    try:
        print (f"1/{i} = {1/i}")
    except ZeroDivisionError:
        print (f"1/{i} = You can't divide by zero !")