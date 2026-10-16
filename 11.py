# Write a Python program to print the sum of the series 1/2+1/3+1/4+ ... +1/N. Where N is a natural number. 
n = int(input("Enter N: "))
total = 0 
for i in range(2, n + 1): 
  total = total + (1 / i)
  print("Sum of series =", total) 
