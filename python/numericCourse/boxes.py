def filledBox(height, width):
    for i in range(height):
        for x in range(width):
            print('+', end=' ')
        print()


def emptyBox(height, width):
    for i in range(width):
        print('+', end=' ')
    print()
    for i in range(height - 2):
        print('+' * (width - (width - 1)), end=' ')
        for x in range(width - 2):
            print(' ', end=' ')
        print('+' * (width - (width - 1)))
    if height > 1:
        for i in range(width):
            print('+', end=' ')


def main():
    while True:
        try:
            height = int(input("How heigh do you want the box: "))
            break
        except ValueError:
            print("Invalid value")
            continue
    while True:
        try:
            width = int(input("How wide do you want the box: "))
            break
        except ValueError:
            print("Invalid value")
            continue
    while True:
        filled = input("Do you want the box filled, [y]es, [n]o: ").lower()
        if filled == 'y':
            filledBox(height, width)
            break
        elif filled == 'n':
            emptyBox(height, width)
            break
        else:
            print("Invalid input")
            continue


if __name__ == "__main__":
    main()
