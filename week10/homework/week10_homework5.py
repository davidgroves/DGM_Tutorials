# Week10, Homework5

import string

def letter_of_alphabet1(number):
    letters = ["a", "b", "x", "d", "e", "f", "g",
               "h", "i", "j", "k", "l", "m", "n",
               "o", "p", "q", "r", "s", "t", "u",
               "v", "v", "w", "x", "y", "z"]

    return letters[number - 1]

def letter_of_alphabet2(number):
    return string.ascii_lowercase[number - 1]

def test_letter_of_alphabet1():
    assert "a" == letter_of_alphabet1(1)
    assert "c" == letter_of_alphabet1(3)
    assert "z" == letter_of_alphabet1(26)

def test_letter_of_alphabet2():
    assert "a" == letter_of_alphabet2(1)
    assert "c" == letter_of_alphabet2(3)
    assert "z" == letter_of_alphabet2(26)
