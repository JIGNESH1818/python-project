# Write a python program to add some days to your present date and print the date added
from datetime import date, timedelta
# timedelta will handle the leap year and also the no of days available in months
days = int(input("Enter number of days to add: "))
today = date.today()
new_date = today + timedelta(days=days) 
print("Today's date:", today)
print("Date after adding days:", new_date) 
