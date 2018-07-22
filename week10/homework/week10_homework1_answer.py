# Week10, Homework1, Answer

import statistics

# Returns the arithmetic mean (average) of a list of numbers.
def mean(list_of_numbers):
    return statistics.mean(list_of_numbers)

def test_mean():
    assert mean([1,2,3,4,5]) == 3
    assert mean([1,3,5,7,9]) == 5
    assert mean([1,2,3,4,5,6]) == 3.5
    assert mean([1.5, 2.5, 3.5, 4.5, 5.5, 6.5]) == 4
