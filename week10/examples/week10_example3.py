# Week10, Example3

def add(x,y):
    return x + y

def test_add_works():
    assert add(2,2) == 4

def test_add_fails():
    assert add(2,3) == 4

test_add_works()
print("The test we expected to work")
test_add_fails()
print("The test we expected to fail")
