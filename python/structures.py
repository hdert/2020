'''
Author: Justin
description: data structures
'''
import random
import sqlite3
from sqlite3 import Error

# Functions
# LVL2 you need to call a function from a function


def main(stats, en_stats):
    '''
    Calling other functions
    params - none
    return - none
    '''
    intro()
    battle(stats, en_stats)


def intro():
    print("""
    Combat system...
    """)


def display_weapons(weapons):
    string = ''
    for i in weapons:
        string = string + \
            f"[{i[0]}]{i[1:]}, {weapons[i][0]} to {weapons[i][1]}; "
    return string[: -1]


def display_stats(stats):
    return f"Your weapons are {display_weapons(stats[0])} your hp is {stats[1]}; and your defense is {stats[2]}"


def battle(stats, en_stats):
    while stats[1] > 0 and en_stats[1] > 0:
        print("You're attacked")
        print(display_stats(stats))
        while attack != 's' or attack != 's' or attack != 'd' or attack != 'b':
            attack = input("Choose your weapon: ").lower()
        rand = random.randint(1, 2)
        if(rand == 1):
            pass
        else:
            pass


# Main
weapons = {'Sword': [15, 20],
           'Staff': [10, 15],
           'Dagger': [3, 8],
           'Bow': [10, 12]}
rand = random.randint(weapons['Sword'][0], weapons['Sword'][1])
print(rand)
hp = 100
dff = 13
if __name__ == "__main__":
    # main([items, hp, dff], [[items[0], items[2], items[3]], hp-20, dff-8])
    print(display_weapons(weapons))
