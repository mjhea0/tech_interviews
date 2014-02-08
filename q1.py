"""
Question 1

The database interface we use within our python layer (psycopg2) returns objects of 
type datetime.datetime (http://docs.python.org/2/library/datetime.html) for any fields 
that are timestamps. 

Write a function that takes in a datetime.datetime and returns one of the following values:

- Just now
- [x] minute(s) ago
- [y] hour(s) ago
- [z] day(s) ago
- [a] week(s) ago
- [b] month(s) ago
- [c] year(s) ago
"""


import datetime


class TimeElapsed(object):

    def __init__(self,dt):
        now = datetime.datetime.now()
        difference = now - dt
        self.year = difference.days / 365
        self.month = difference.days / 30 - (12 * self.year)
        if self.year > 0:
            self.day = 0
        else: 
            self.day = difference.days % 30
        self.hour = difference.seconds / 3600
        self.minute = difference.seconds / 60 - (60 * self.hour)

    def output(self):
        if self.minute < 1:
            return "Just now"
        else:
            results = []
            for period in ['year', 'month', 'day', 'hour', 'minute']:
                value = getattr(self, period)
                if value:
                    if value > 1:
                        period += "s"
                    results.append("%s %s" % (value, period))
            return ", ".join(results) + " ago"


test = TimeElapsed(datetime.datetime(2014, 2, 5, 0, 36, 0))
print test.output()
