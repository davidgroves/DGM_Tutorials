# Week8, Example5

import datetime

venus_birthday = datetime.datetime(year=1980, month=6, day=17)
serena_birthday = datetime.datetime(year=1981, month=9, day=26)

print(venus_birthday)
print(serena_birthday)
print(serena_birthday - venus_birthday)

current_datetime = datetime.datetime.now()
next_us_election = datetime.datetime(year=2020, month=11, day=3)

print(next_us_election - current_datetime)
