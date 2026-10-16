# Write a function that count number of digits in a number. 
def count_digits(num): 
  count = 0  
  while num > 0: 
    count = count + 1 
    num = num // 10  
    return count
    num = int(input("Enter a number: ")) 
    result = count_digits(num) 
    print("Number of digits =", result)
