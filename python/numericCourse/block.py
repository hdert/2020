def main(uChoice):
    i = 1
    x = 0
    while x <= 100:
        if i % uChoice == 0:
            x += 1
        i += 1
    maxLength = len(str(i)) + 1
    i = 1
    x = 0
    z = 1
    while x < 100:
        if i % uChoice == 0:
            print(f"{i:4}", end='')
            x += 1
            z += 1
        if z % 11 == 0:
            print()
            z = 1
        i += 1


if __name__ == "__main__":
    while True:
        try:
            uChoice = int(input("Pick a multiple: "))
            break
        except ValueError:
            print("Invalid value, needs number")
            continue
    main(uChoice)
