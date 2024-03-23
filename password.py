import random
import string

def generate_password(length=12, with_digits=True, with_symbols=True):
    if length < 12:
        print("It's recommended to use a password length of at least 12 characters for better security.")
        length = 12  

    characters = string.ascii_letters 
    if with_digits:
        characters += string.digits
    if with_symbols:
        characters += string.punctuation
        
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired password length (minimum 12): "))
        if length < 12:
            print("Minimum length is set to 12 for security reasons.")
            length = 12
    except ValueError:
        print("Invalid input. Using default length of 12.")
        length = 12

    with_digits = input("Include digits? (y/n): ").lower() == 'y'
    with_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, with_digits, with_symbols)
    print(f"Generated Password: {password}")
