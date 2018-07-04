# Week10, Example8

def add(x,y):
    return x + y

def multiply(x,y):
    i = 1
    answer = x
    while i < y:
        answer += x
        i += 1
    return answer

def subtract(x,y):
    return x - y

def test_add():
    assert add(2,2) == 4

def test_multiply():
    assert multiply(2,2) == 4
    assert multiply(2,5) == 10
    assert multiply(8,8) == 64

def test_subtract():
    assert subtract(4,2) == 2
