# Week10, Example4

def add(x,y):
    return x + y

def multiply(x,y):
    return x * y

def test_add_works():
    assert add(2,2) == 4

def test_add_fails():
    assert add(2,3) == 4

def test_multiply_works():
    assert multiply(2,2) == 4

def test_multiply_fails():
    assert multiply(2,3) == 4
