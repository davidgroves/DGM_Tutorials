# Week10, Homework5, Answer

import datetime

def day_of_week(day, month, year):
    day_list = ["Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday"]

    day = datetime.date(day=day, month=month, year=year)
    return(day_list[day.weekday()])

def test_day_of_week():
    assert "Tuesday" == day_of_week(3,7,2018)
    assert "Saturday" == day_of_week(1,1,2000)
    assert "Wednesday" == day_of_week(29,2,2012)
