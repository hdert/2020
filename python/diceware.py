from random import randint as rand

times = int(input("How many words would you like? "))

for x in range(0, times):
    for y in range(0, 4):
        print(rand(1, 6), end='')

        if y == 3:
            print(rand(1, 6), end='\n')
