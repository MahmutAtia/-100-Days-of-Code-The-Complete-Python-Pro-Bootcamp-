import datetime as dt
import random

now = dt.datetime.now()
day = now.day
print(day)
if day == 28:
    with open("quotes.txt") as f:
        lines =  f.readlines()
        print(random.choice(lines))

