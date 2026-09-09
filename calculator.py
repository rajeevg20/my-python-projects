while True:
    while True:
        try:
            a = float(input("please enter first number: "))
            break
        except ValueError:
            print("please enter a valid first number")

    while True:
        op = input("please enter your operator like +, -, *, /: ")
        if op in ["+", "-", "*", "/"]:
            break
        else:
            print("please enter correct operator")

    while True:
        try:
            b = float(input("please enter second number: "))

            if op != "/" or b != 0:
                break
            else:
                print("division with zero is undefined, please select second number other than 0")

        except ValueError:
            print("please enter a valid second number")

    if op == "+":
        print(f"result = {a + b}")
    elif op == "-":
        print(f"result = {a - b}")
    elif op == "/":
        print(f"result = {a / b}")
    else:
        print(f"result = {a * b}")

    while True:
        c = input("calculate again? y/n: ")

        if c == "y":
            break

        elif c == "n":
            break

        else:
            print("please enter y or n")

    if c == "n":
        break