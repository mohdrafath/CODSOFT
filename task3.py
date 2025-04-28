# Task 3 - Password Generator
import random
import string

def generate_password():
    print("Password Generator\n")
    
    # Get password length with validation
    while True:
        try:
            length = int(input("Enter password length (8-128): "))
            if 8 <= length <= 128:
                break
            print("Please enter a number between 8 and 128")
        except ValueError:
            print("Invalid input! Please enter a number.")

    # Character set configuration
    chars = string.ascii_lowercase  # Always include lowercase
    
    # Complexity options
    if input("Include uppercase letters? (y/n): ").lower() == 'y':
        chars += string.ascii_uppercase
        
    if input("Include numbers? (y/n): ").lower() == 'y':
        chars += string.digits
        
    if input("Include special characters? (y/n): ").lower() == 'y':
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"

    # Generate password securely
    secure_random = random.SystemRandom()
    password = [secure_random.choice(chars) for _ in range(length)]
    
    # Shuffle for extra randomness
    secure_random.shuffle(password)
    final_password = ''.join(password)

    # Display result
    print("\n" + "="*40)
    print(f"Generated Password: {final_password}")
    print("="*40 + "\n")

if __name__ == "__main__":
    generate_password()
