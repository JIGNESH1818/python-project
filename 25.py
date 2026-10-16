# Write a function for finding factors (n) and use factors function to check whether a given number n is prime or not.
def factors(n):  
  result = []   
  for i in range(1, n + 1):  
    if n % i == 0:       
      result.append(i) 
      return result 
      num = int(input("Enter a number: "))
      f = factors(num) 
print("Factors:", f) 
if len(f) == 2: 
  print("Prime Number")
else:
  print("Not a Prime Number") 
