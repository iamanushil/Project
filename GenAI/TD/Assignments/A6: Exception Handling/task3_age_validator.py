# Task 3: Custom Exception - Age Validator
# check_age(age) raises ValueError if age not in 1–120; main uses try/except.

def check_age(age):
    if age < 1 or age > 120:
        raise ValueError("Age must be between 1 and 120")


user_input = input("Enter age: ")
try:
    age = int(user_input)
    check_age(age)
    print("Age is valid:", age)
except ValueError as e:
    print(e)
