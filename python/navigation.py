'''
Author: Justin Muirhead
'''

room = 0

rooms = ['Hall', 'Hall2', 'Courtyard', 'Hall3', 'Kitchen', 'Hall4', 'Hall5', 'Bedroom', 'CheeseRoom']

desc = ['Hall with carpet', 'Hall with paintings', 'Courtyard with paving stones', 'Hallway with plants', 'Kitchen has old moldy food', 'Hallway has rat droppings', 'Hallway has dusty cobwebs', 'Bedroom has a bed in it', 'Has cheese in it']

n = [1, 2, 3, 4, 99, 99, 99, 99, 99]

s = [99, 0, 1, 2, 3, 99, 99, 99, 99]

e = [99, 99, 6, 99, 99, 2, 8, 5, 99]

w = [99, 99, 5, 99, 99, 7, 2, 99, 6]

while True:
  print("You are in", rooms[room], desc[room])

  if n[room] != 99:
    print("You can go north")

  if s[room] != 99:
    print("You can go south")

  if e[room] != 99:
    print("You can go east")

  if w[room] != 99:
    print("You can go west")

  move = input("Enter [n][s][e][w]: ")

  if move == 'n':
    room = n[room]
  elif move == 's':
    room = s[room]
  elif move == 'e':
    room = e[room]
  elif move == 'w':
    room = w[room]
