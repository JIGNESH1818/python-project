# Create a dictionary that accepts cricket players’names and scores in a match. Also we are retrieving runs by entering the player’s name.
# Create an empty dictionary
players = {} 
# Accept player names and scores
n = int(input("Enter number of players: ")) 
for i in range(n):  name = input("Enter player name: ")    
score = int(input("Enter score: "))     players[name] = score 
# Display dictionary 
print("\nPlayers and Scores:") print(players)
# Retrieve runs by entering player's name 
search_name = input("\nEnter player name to find score: ")
if search_name in players:
  print(search_name, "scored", players[search_name], "runs.") 
else: print("Player not found.") 
