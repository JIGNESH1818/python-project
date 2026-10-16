# Write a Python program to check whether a number is an Armstrong number or not. 
# 153 = (1*3 + 5*3 + 3*3) = 153 where 3 is length
num = int(input("Enter a number: ")) 
temp = num
len = len(str(num)) 
total = 0 
while temp > 0:
digit = temp % 10 
#print(digit) 
total = total + digit ** len 
#print(total) 
temp = temp // 10 
#print(temp)
if total == num: 
  print("Armstrong Number") else:  
  print("Not an Armstrong Number") 
