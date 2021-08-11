import datetime

# Format the entered year, month and day in a human-readable way. (if the month has 1 digit, it only has 1 digit. If you add 0 before, it will throw an error)
d = datetime.date(2016,7,24)
print(d)

# Get today date
tday = datetime.date.today()
print(tday)

# Grab just the year/day/month
print(tday.year)
print(tday.day)
print(tday.month)

# You can even grab the week day
# In this method, Monday is 0 and Sunday is 6
print(tday.weekday())
# In this method, Monday is 1, Sunday is 7
print(tday.isoweekday())

# Interact the difference between 2 dates and time.
tdelta = datetime.timedelta(days=7)
	# Print out what the day will be 1 week from now
print(tday + tdelta)
	
	# Print out what the day will be 1 week before
print(tday - tdelta)

# date2 is equal to date1 plus timedelta
# timedelta = date1 + date2 


bday = datetime.date(2021,7,26)
till_bday = bday - tday
# Print the total_seconds until my birthday.
print(till_bday.total_seconds())

# Year, month, day
t = datetime.date(2016,7,26)

# Work with hours, minutes, seconds and miliseconds 
t = datetime.time(9,30,45,100000)
print(t) # Print out the time

# Access to everything
dt = datetime.datetime(2016,6,26,12,30,45,10000)
print(dt)

# Access just the date
print(dt.date())

# Access just the time
print(dt.time())
# This also works with .year, .hour, .month

# You can even work with timedelta with these
tdelta = datetime.timedelta(days=7) # This is the same as years, months, hours, minutes, etc.
print(tdelta + dt)
print()

dt_today = datetime.datetime.today() # Return local datetime with 0 timezone

dt_now = datetime.datetime.now() # Give an option to pass the time zone. If none is passed, the results is the same as .today()

dt_utcnow = datetime.datetime.utcnow() # Give us the current UTC but with none timezone

print(dt_today)
print(dt_now)
print(dt_utcnow)

import pytz
# Make the timezone aware
dt = datetime.datetime(2016,7,26,12,30,45,tzinfo=pytz.UTC)
print(dt)
# Output: 2016-07-26 12:30:45+00:00

# Pass a timezone to now() and you will see the current UTC time
dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)
# 2021-07-24 09:14:44.912584+00:00

# Get the current UTC time in a timezone aware but with a different way. The ouput is the same as before.
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)

# Change to a new timezone
# dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
# print(dt_mtn)
# Output: 2021-07-24 03:18:02.475553-06:00. -06:00 is the different between my time and the new timezone.

# Print out all the timezone
for tz in pytz.all_timezones:
	print(tz)


# Create a new local datetime without timezone information
dt_mtn = datetime.datetime.now()

# Convert to a new timezone with a naive time will generate an error. But wtf, why don't I have any error? This is because as Python 3.6, this won't an error anymore.
dt_east = dt_mtn.astimezone(pytz.timezone("US/Eastern"))
print(dt_mtn)

# Localize the timezone
mtn_tz = pytz.timezone("US/Mountain")
dt_mtn = mtn_tz.localize(dt_mtn)
print(dt_mtn)

# So you can print without any error?
dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
print(dt_east)


# The best way to parse datetime and use it in eternal use:
print(dt_mtn.isoformat())

# Format the datetime and find the format code you want in the documentation. https://docs.python.org/3.9/library/datetime.html#strftime-and-strptime-format-codes
# Basically, convert datetime to string
print(dt_mtn.strftime('%B %d, %Y'))
# Output: July 24, 2021

# Convert string to datetime.
dt_str = "July 24, 2021"

# First argument is a string, the second is the format of the string arccoding to the documentation. https://docs.python.org/3.9/library/datetime.html#strftime-and-strptime-format-codes
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')

print(dt)
















