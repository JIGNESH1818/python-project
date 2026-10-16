# Write a python program to print date, time for today and now.
from datetime import datetime 
now = datetime.now() 
print("Today's Date:", now.date()) 
print("Current Time:", now.time())
print("Date and Time:", now) 
