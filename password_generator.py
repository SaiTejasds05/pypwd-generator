import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special_chars=True):
    # Define character sets
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if use_uppercase else ''
    number_chars = string.digits if use_numbers else ''
    special_chars = '!@#$%^&*()_+-=[]{}|;:,.<>?' if use_special_chars else ''
    
    # Combine all allowed characters
    all_chars = lowercase_chars + uppercase_chars + number_chars + special_chars
    
    # Ensure at least one character from each selected type
    password = []
    if use_uppercase:
        password.append(random.choice(uppercase_chars))
    if use_numbers:
        password.append(random.choice(number_chars))
    if use_special_chars:
        password.append(random.choice(special_chars))
    password.append(random.choice(lowercase_chars))  # Always include lowercase
    
    # Fill the rest of the password length
    remaining_length = length - len(password)
    password.extend(random.choice(all_chars) for _ in range(remaining_length))
    
    # Shuffle the password characters
    random.shuffle(password)
    
    # Join and return the password
    return ''.join(password)

def main():
    print("Welcome to Password Generator!")
    
    # Get user preferences
    try:
        length = int(input("Enter password length (minimum 8): "))
        if length < 8:
            length = 8
            print("Password length set to minimum of 8 characters.")
    except ValueError:
        length = 12
        print("Invalid input. Using default length of 12 characters.")
    
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    
    # Generate and display password
    password = generate_password(
        length=length,
        use_uppercase=use_uppercase,
        use_numbers=use_numbers,
        use_special_chars=use_special_chars
    )
    
    print("\nGenerated Password:", password)
    print("Password length:", len(password))

if __name__ == "__main__":
    main() 