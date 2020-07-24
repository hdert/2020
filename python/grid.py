'''
Author: Justin Muirhead
Description: Layouts and Grids
'''

# Variables 

grid = [
    ['_','_','_'],
    ['_','_','_'],
    ['_','_','_']
  ]

gridInfo = {
  'x': '3',
  'y': '3'
}

# Functions

def display(displayList):
  print('-------------')
  for i in displayList:
    print('|', end=' ')
    for j in i:
      print(j, end=' | ')
    print('\n-------------')
def resetGrid():
  return [
    ['_','_','_'],
    ['_','_','_'],
    ['_','_','_']
  ]
def choiceValidity(input):
  return input
def askForName(player):
  pass
def intro():
  print('''
Welcome to Naughts & Crosses.
Naughts & Crosses is a game about getting three in a row.
You do this by choosing the coordinates of your marker,
Player One's marker is 0 and Player Two's marker is X.
It is turn based with Player One starting the game.
The game will prompt you for the value of each coordinate.
''')
# Main

# Print introduction

intro()

# Display the grid

display(grid)

# Ask for Player One's name

p1Name = askForName("Player One")

# Player One chooses their 0

choice = checkValidity(split(input())
grid[choice[0]][choice[1]] = ['X','X']
display(grid)

# Check that player selection is valid and avalible

#if(grid[choice] == '_'):
#  pass

# Write to the grid



# Display the grid



# Check if a player has won

  # Ask for players name
    # Check that player name doesn't already exist
    # Add points to leaderboard in the players name
    # Display leaderboard
    # Ask if they want to play again


# Check if board is full

  # Display leaderboard
  # Ask if they want to play again

# Ask for Player Two's name
# Repeat Choice but with Player Two and X

