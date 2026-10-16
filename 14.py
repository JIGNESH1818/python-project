# Write a Python program to swap first and last digits of a number.
num = int(input("Enter a number: ")) 
s = str(num)  
if len(s) == 1:
  result = s
else:
  result = s[-1] + s[1:-1] + s[0] 
  print("Number after swapping:", result) 
