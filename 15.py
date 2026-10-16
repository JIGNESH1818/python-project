# Write a Python program for printing prime numbers up to N. (N>100). 
n = int(input("Enter N: "))
print("Prime numbers:")  
for num in range(2, n + 1): 
  is_prime = True  
  for i in range(2, num):    
    if num % i == 0:   
      is_prime = False    
      break     
      if is_prime: 
        print(num, end=" ") 
