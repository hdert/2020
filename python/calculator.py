print("This is an addition calculator")
while True:
    try:
        print("Input your first number, press enter, then input your second number, press enter.")
        print("Your result is: {}".format(float(input()) + float(input())))
        break
    except ValueError:
        print("Sorry but your input wasn't in the correct format.")