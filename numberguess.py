import random as rd
secret_number = rd.randint(1,20)
print("secret number is:", secret_number)

while True:
    try:
        level = int(input("choose the difficulty level, enter 1 for easy or 2 for hard: "))
        if level == 1:
            n = 10
            break
        elif level == 2:
            n = 5
            break
        else:
            print("error, enter 1 or 2")
    except ValueError:
        print("please enter a number 1 or 2")

print(f"you have {n} attempts")

for i in range(1, n+1):
    try:
        while True:
            guess_number = int(input("Guess an integer between 1 to 20: "))
            if guess_number in range(1, 21):
                break
            else:
                print("enter a number between 1 to 20")
        if guess_number == secret_number:
            print("You guessed the number correctly")
            break
        elif guess_number > secret_number:
            print(f"sorry your guess is higher than secret number, you have {n-i} more attempt")
        else:
            print(f"sorry your guess is lower than secret number, you have {n-i} more attempt")
    except ValueError:
        print("please enter a number between 1 to 20")
else:
    print(f"Game over! You didn't guess the number. secret number was: {secret_number}")
