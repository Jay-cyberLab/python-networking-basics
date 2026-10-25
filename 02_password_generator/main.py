import random
import string
import secrets

def ask_yes_no(question):
    while True:
        answer = input(question).lower()

        if answer == "yes" or answer == "no":
            return answer
        else:
            print("Please Type yes or no.")


def generate_password(length,selected_groups):
    password_characters = []

    #Guarantess at least one character from every selected group
    for group in selected_groups:
        password_characters.append(secrets.choice(group))

    all_characters = "".join(selected_groups)

    while len(password_characters) < length:
        password_characters.append(secrets.choice(all_characters))

    secrets.SystemRandom().shuffle(password_characters)

    return "".join(password_characters)

while True:
    user_input = input("Enter password length : ")
    
    if user_input.isdigit():
        length = int(user_input)
        
        if length >= 4:
            break
        else:
            print("Password length must be at least 4.")
    else:
        print("Please enter a valid number.")

selected_groups = []

include_letters = ask_yes_no("Include letters? (yes/no) : ")
include_numbers = ask_yes_no("Include numbers? (yes/no) : ")
include_symbols = ask_yes_no("Include symbols? (yes/no) : ")

if include_letters == "yes":
    selected_groups.append(string.ascii_letters)

if include_numbers == "yes":
    selected_groups.append(string.digits)

if include_symbols == "yes":
    selected_groups.append(string.punctuation)

if len(selected_groups) == 0:
    print("You must choose at least one character type.")
elif length < len (selected_groups):
    print("Password length is too short for your selected character type.")
else:
    new_password = generate_password(length, selected_groups)
    print(f"\nGenerated password : {new_password}")

