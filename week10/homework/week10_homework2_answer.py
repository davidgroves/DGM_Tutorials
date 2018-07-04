# Week10, Homework2, Answer

# Take a length of time in days, mins and hours
# and return how long it takes in seconds.
def time_in_seconds(days=0, hours=0, mins=0):
    return(days * 86400 + hours * 3600 + mins * 60)

def test_time_in_seconds():
    assert time_in_seconds(days=1, hours=0, mins=0) == 86400
    assert time_in_seconds(days=1, hours=15, mins=35) == 142500
    assert time_in_seconds(days=2, hours=3, mins=11) == 184260
