print("This is an addition calculator")
while True:
    try:
        print("Input your first number, press enter, then input your second number, press enter.")
        conditionOne = float(input())
        conditionTwo = float(input())
        result = conditionOne + conditionTwo
        print("Your result is: {}".format(result))
        break
    except ValueError:
        print("Sorry but your input wasn't in the correct format.")