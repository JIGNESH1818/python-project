# Write a Python program that prompts users to enter numbers.
# The process will repeat until user enters. Finally, the program prints the sum of the numbers entered by the user. 
total = 0
while True:  
  num = int(input("Enter a number (0 to stop): ")) 
if num == 0: 
    break  
total = total + num  
print("Sum =", total) 
