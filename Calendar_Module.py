import calendar

# get input - space separated numbers for month, day, year
mo, dy, yr = map(int, input().split())

# create tuple with days of the week - this is a 'lookup' for converting
# the number of the day into the string of the day
weekdays = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')

# use the calendar.weekday function to return the integer number of the day.
day = weekdays[calendar.weekday(yr, mo, dy)]
print(day.upper())