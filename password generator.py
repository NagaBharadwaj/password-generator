import random
import string

def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        num_passwords = int(input("Enter the number of passwords you want to generate: "))
        length = int(input("Enter the length of the passwords: "))
        
        if num_passwords <= 0 or length <= 0:
            print("Both the number of passwords and the length should be positive integers.")
            return
        
        print("\nGenerated Passwords:")
        for i in range(num_passwords):
            print(f"Password {i + 1}: {generate_password(length)}")
    except ValueError:
        print("Please enter valid integers for the number of passwords and the length.")

if __name__ == "__main__":
    main()
