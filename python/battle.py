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


def weapon_first_to_full(weapons):
    first_to_full = {}
    for i in weapons:
        first_to_full.update({i[0].lower(): i})
    return first_to_full


def get_weapon(weapons):
    while True:
        weapon = input("Choose your weapon: ").lower()
        first_to_full = weapon_first_to_full(weapons)
        for i in first_to_full:
            if weapon == i:
                return first_to_full[i]


def get_damage(weapons, en_dff, weapon):
    damage = random.randint(weapons[weapon][0], weapons[weapon][1])
    damage -= round(damage * (en_dff / 100), 2)
    return damage


def damage_report(hp, en_hp):
    return f"You have {hp}hp, the enemy has {en_hp}hp"


def battle(stats, en_stats):
    attack = ''
    print("You're attacked")
    print(display_stats(stats))
    weapon = get_weapon(stats[0])
    while stats[1] > 0 and en_stats[1] > 0:
        rand = random.randint(1, 2)
        if(rand == 1):
            damage = get_damage(stats[0], en_stats[2], weapon)
            en_stats[1] -= damage
            en_stats[1] = round(en_stats[1], 2)
            print(f"You attack enemy inflicting {damage}hp")
            print(damage_report(stats[1], en_stats[1]))
        else:
            en_damage = get_damage(en_stats[0], stats[2], 'Dagger')
            stats[1] -= en_damage
            stats[1] = round(stats[1], 2)
            print(f"The enemy attacks you inflicting {en_damage}hp")
            print(damage_report(stats[1], en_stats[1]))
    if stats[1] > 0:
        print("You win!")
    else:
        print("You die!")


# Main
weapons = {'Sword': [15, 20],
           'Mom': [10, 15],
           'Dagger': [3, 8],
           'Bow': [10, 12]}
en_weapons = {'Sword': [15, 20],
              'Dagger': [3, 8],
              'Bow': [10, 12]}
hp = 100
dff = 13
if __name__ == "__main__":
    main([weapons, hp, dff], [en_weapons, hp, dff])
