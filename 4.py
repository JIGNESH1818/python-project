# Write a Python program to find the maximum between three numbers.....
a = int(input("Enter first number: "))
b = int(input("Enter second number: ")) 
c = int(input("Enter third number: "))  
if a >= b and a >= c:    
maximum = a 
elif b >= a and b >= c: 
maximum = b else:   
maximum = c 
print("Maximum number =", maximum) 
