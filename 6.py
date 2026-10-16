# Write a Python program to print all the numbers from 1 to 1000 that are not divisible by 2, 3, 5, 7, 11, 13, 17 and 19. 
for num in range(1, 1001):
if (num % 2 != 0 and
num % 3 != 0 and
num % 5 != 0 and
num % 7 != 0 and 
num % 11 != 0 and 
num % 13 != 0 and 
num % 17 != 0 and
num % 19 != 0):    
print(num) 
