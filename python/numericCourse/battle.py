from random import randint as rand


def printStats(hp, en_hp):
    print(f"\nYou have {hp} health\nThe orc has {en_hp} health")


def main(hp, en_hp):
    atk_min = 1
    atk_max = 20
    miss_chance = 4
    en_miss_chance = 2
    printStats(hp, en_hp)
    if rand(1, en_miss_chance) != 1:
        en_atk = rand(atk_min, atk_max)
    else:
        en_atk = 0
    while True:
        action = input('''
[a]ttack
[d]efend
: ''').lower()
        if action == 'a':
            atk = rand(atk_min, atk_max)
            if rand(1, miss_chance) != 1:
                print(f"You attack the orc dealing {atk} damage!")
            else:
                print("You missed!")
                atk = 0
            en_hp -= atk
            break
        elif action == 'd':
            if en_atk != 0:
                if rand(1, 2) == 1:
                    print(
                        f"You block with your shield blocking {en_atk} damage and rebounding it onto the orc!"
                    )
                    en_hp -= en_atk
                    en_atk = 0
                else:
                    print("You don't put up the shield in time!")
            break
        else:
            print("Invalid input")
            continue
    if en_atk != 0:
        print(f"The orc attacks with an axe dealing {en_atk}")
        hp -= en_atk
    else:
        print("The orc misses")
    if hp > 0 and en_hp > 0:
        main(hp, en_hp)
    elif hp <= 0:
        print("You lose!")
    elif en_hp <= 0:
        print("You win!")


hp = 50
en_hp = 100

if __name__ == "__main__":
    print("You're face to face with an angry orc")
    main(hp, en_hp)
