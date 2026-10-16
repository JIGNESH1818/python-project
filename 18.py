# Write a python program to count the number of characters in the string and store them in a dictionary data structure 
text = input("Enter a string: ")
frequency = {}
for char in text:
  if char in frequency: 
    frequency[char] = frequency[char] + 1
  else:   
    frequency[char] = 1 
    print("Character frequency:")
    print(frequency) 
