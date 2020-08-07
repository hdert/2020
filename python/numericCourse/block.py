def main(uChoice):
    for x in range(10):
        for i in range(1, 11):
            print(
                f"{(x * 10 + i) * uChoice:{len(str(100 * uChoice))}}", end=' ')
        print()


if __name__ == "__main__":
    while True:
        try:
            uChoice = int(input("Pick a multiple: "))
            break
        except ValueError:
            print("Invalid value, needs number")
            continue
    main(uChoice)
