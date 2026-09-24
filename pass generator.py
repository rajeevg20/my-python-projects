import string
upperletters = string.ascii_uppercase
lowerletters = string.ascii_lowercase
digits = string.digits
punct = string.punctuation
total = upperletters + lowerletters + digits + punct
print(total)
import random as rd
def get_password_length():
    while True:
        length = int(input("Tell the length of Password: "))
        if length < 8:
            print("minimum 8 characters required")
        else:
            return length
def generate_password(length):
    password = rd.choice(upperletters) + rd.choice(lowerletters) + rd.choice(digits) + rd.choice(punct)
    for _ in range(length-4):
        char = rd.choice(total)
        password = password + char
    lst = list(password)
    rd.shuffle(lst)
    result = "".join(lst)
    return result

def validate_password(password):
    uppercase_valid = False
    lowercase_valid = False
    digit_valid = False
    punct_valid = False
    for p in password:
        if p in upperletters:
            uppercase_valid = True
        elif p in lowerletters:
            lowercase_valid = True
        elif p in digits:
            digit_valid = True
        elif p in punct:
            punct_valid = True
    password_valid = uppercase_valid and lowercase_valid and digit_valid and punct_valid
    # valid = bool(uppercase_valid * lowercase_valid * digit_valid * punct_valid)
    return {"password_valid":password_valid, "uppercase_valid":uppercase_valid, "lowercase_valid":lowercase_valid, "digit_valid":digit_valid, "punct_valid":punct_valid}

def print_validation_details(uppercase_valid, lowercase_valid, digit_valid, punct_valid):
    if not uppercase_valid:
        print("uppercase missing")
    if not lowercase_valid:
        print("lowercase missing")
    if not digit_valid:
        print("digits missing")
    if not punct_valid:
        print("punctuation missing")

length = get_password_length()
password = generate_password(length)
print(f"Your password is {password}")
validation = validate_password(password)
print(f"password valid: {validation['password_valid']}")
print_validation_details(validation["uppercase_valid"], validation["lowercase_valid"], validation["digit_valid"], validation["punct_valid"])




