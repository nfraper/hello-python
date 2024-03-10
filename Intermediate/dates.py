### Dates ###

from datetime import datetime

now = datetime.now()

year_2023 = datetime(2023, 1, 1)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())
    
    
print_date(now)
print_date(year_2023)


from datetime import time

current_time = time()
print(current_time)

current_time = time(21, 6, 0)
print(current_time)


from datetime import date

current_date = date.today()
print(current_date)

print(current_date - year_2023.date())


from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks=10)
print(start_timedelta)