import datetime
import pytz
a = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
b = "Sample String"

# The goal of __repr__ is to be unambiguous
# The goal of __str__ is to be readable

print(str(a))
# Output: 2021-07-27 09:13:41.901943+00:00

print(repr(a)) # It is used to debugging and logging.
# Output:  datetime.datetime(2021, 7, 27, 9, 13, 41, 901943, tzinfo=<UTC>)

print(str(b))
print(repr(b))