# Week8, Example6

import datetime

venus_birthday = datetime.datetime(year=1980, month=6, day=17)
serena_birthday = datetime.datetime(year=1981, month=9, day=26)

weekdays = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

print(venus_birthday.weekday())
print(serena_birthday.weekday())

print(weekdays[venus_birthday.weekday()])
print(weekdays[serena_birthday.weekday()])
