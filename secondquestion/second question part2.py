# Exercise 3

# Import related libraries
from datetime import datetime, timedelta

class range:
    def __init__(self, s_date: datetime, e_date: datetime, w_day: int):
        self.s_date = s_date
        self.e_date = e_date
        self.w_day = w_day

    def __iter__(self):
        self.s_date = self.s_date
        return self

    def __next__(self):
        diff_week = self.w_day - self.s_date.weekday()
        temp_date = datetime(year=self.s_date.year, month=self.s_date.month, day=(self.s_date.day + diff_week))
        if temp_date >= self.s_date:
            return temp_date

        while temp_date <= self.e_date:
            temp_date = temp_date + timedelta(days=7)
            if temp_date > self.e_date:
                print("End")
                break
            return temp_date



