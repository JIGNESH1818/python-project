 # Write a program to find the sum of all odd numbers between 1 to n.
n = int(input("Enter N: "))
total = 0  
for i in range(1, n + 1, 2):   
  total = total + i
  print("Sum of odd numbers =", total) 
