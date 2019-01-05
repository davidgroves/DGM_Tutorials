def double(f):
    def inner_double(*args, **kwargs):
        return 2 * f(*args, **kwargs)
    return inner_double

@double
def two():
    return 2

@double
@double
def three():
    return 3

print(two())
print(three())