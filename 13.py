# Write a Python program to find HCF (GCD) of two numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
while b != 0:
  remainder = a % b 
  a = b
  b = remainder 
  print("HCF / GCD =", a) 
