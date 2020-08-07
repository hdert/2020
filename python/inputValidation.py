while True:
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Invalid value, enter an integer")
        continue
    except:
        print("Something went wrong")
        continue
    if age < 0 or age > 499:
        print("Age not within valid range")
        continue
    else:
        break
