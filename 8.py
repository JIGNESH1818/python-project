# Write a python program for filter() to filter only even numbers from a given list. 
#Example: 6 = 1 + 2+ 3 check the factor
num = int(input("Enter a number: ")) 
total = 0
for i in range(1, num):
  if num % i == 0:     
    total = total + i
    if total == num:
      print("Perfect Number") 
    else:   
      print("Not a Perfect Number") 
