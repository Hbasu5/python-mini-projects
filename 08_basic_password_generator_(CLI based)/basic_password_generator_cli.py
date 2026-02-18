#PASSWORD GENERATOR (CLI VERSION)
import random
import string

def password_generator(length):
    characters=string.ascii_letters+string.digits
    password=""
    for _ in range(length):
        password+=random.choice(characters)
    return password

while True:
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            print("Please enter a positive integer for the password length.")
            continue
    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")
        continue

    obtained_password = password_generator(length)
    print("Generated password:", obtained_password)

    print("Do you want to generate another password? Y/N ")
    ch = input().lower()
    if ch != "y":
        print("Exiting the password generator. Goodbye!")
        break
