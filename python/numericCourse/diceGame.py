from random import randint as rand


def main(turn, total):
    print(f"\nRoll {turn}\n")
    roll = [0, 0]
    roll[0], roll[1] = rand(1, 6), rand(1, 6)
    score = roll[0] + roll[1]
    if score == 2:
        print("You get a Snake Eyes!")
        print(f"Your total is {total}")
        while True:
            playAgain = input("Would you like to play again? [y]es, [n]o: ")
            if playAgain == 'y':
                main(1, 0)
                return
            elif playAgain == 'n':
                print("See you again soon!")
                return
            else:
                print("Invalid input")
                continue
    else:
        total += score
        print(f"You roll a {roll[0]} and a {roll[1]}")
        print(f"Your score is {score}, and your total is {total}")
        while True:
            playAgain = input("Would you like to roll again, [y]es, [n]o: ")
            if playAgain == 'y':
                main(turn + 1, total)
                return
            if playAgain == 'n':
                print("See you again soon!")
                return
            else:
                print("Invalid input")
                continue


if __name__ == "__main__":
    print('''
This is a game about rolling two dice,
the goal is to get the highest score,
the only problem being is that if you
roll two one's 'Snake Eyes', you lose.''')
    main(1, 0)
