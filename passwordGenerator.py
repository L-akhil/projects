import string
import random

def generate_password(length=12):
    # Define character sets for each type of character
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    try:
        num_passwords = int(input("Enter the number of passwords to generate: "))
        length = int(input("Enter the length of each password: "))

        if num_passwords <= 0 or length <= 0:
            print("Please enter valid numbers greater than zero.")
            return

        for _ in range(num_passwords):
            password = generate_password(length)
            print(password)

    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
