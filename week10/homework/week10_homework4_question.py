# Week10, Homework4, Answer

import datetime

def day_of_week(day, month, year):
    day_list = ["Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday"]

    day = datetime.date(day=day, month=month, year=year)
    return(day_list[day.weekday()])

def test_day_of_week():
    # Put your tests here.
    pass
