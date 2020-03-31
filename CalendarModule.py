import calendar
Date = [int(i) for i in input().split()]
print((calendar.day_name[calendar.weekday(Date[2],Date[0],Date[1])]).upper())