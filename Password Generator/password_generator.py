import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_symbols=True):
    """Generate a random password with the given length and complexity options."""
    
    # Build the character pool
    characters = string.ascii_lowercase  # Always include lowercase

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected.")

    # Ensure at least one character from each selected category
    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))
    password.append(random.choice(string.ascii_lowercase))

    # Fill remaining length with random characters
    remaining = length - len(password)
    password += random.choices(characters, k=remaining)

    # Shuffle to avoid predictable pattern at the start
    random.shuffle(password)

    return ''.join(password)


def get_yes_no(prompt):
    """Prompt user for a yes/no answer."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ('y', 'yes'):
            return True
        elif answer in ('n', 'no'):
            return False
        else:
            print("  Please enter 'y' or 'n'.")


def get_password_length():
    """Prompt user for a valid password length."""
    while True:
        try:
            length = int(input("Enter desired password length (minimum 4): ").strip())
            if length < 4:
                print("  Password length must be at least 4.")
            else:
                return length
        except ValueError:
            print("  Please enter a valid number.")


def main():
    print("=" * 45)
    print("       🔐  PASSWORD GENERATOR  🔐")
    print("=" * 45)

    # Get password length
    length = get_password_length()

    # Get complexity options
    print("\nCustomize complexity (press Enter to accept defaults):")
    use_uppercase = get_yes_no("  Include uppercase letters? (Y/n): ")
    use_digits    = get_yes_no("  Include digits (0–9)?          (Y/n): ")
    use_symbols   = get_yes_no("  Include symbols (!@#...)?      (Y/n): ")

    # Generate the password
    try:
        password = generate_password(length, use_uppercase, use_digits, use_symbols)
    except ValueError as e:
        print(f"\n❌ Error: {e}")
        return

    # Display the result
    print("\n" + "=" * 45)
    print(f"  Generated Password:  {password}")
    print("=" * 45)

    # Strength indicator
    strength = "Weak"
    if length >= 12 and use_uppercase and use_digits and use_symbols:
        strength = "Strong 💪"
    elif length >= 8 and (use_uppercase or use_digits or use_symbols):
        strength = "Moderate ⚠️"

    print(f"  Password Length  :  {length} characters")
    print(f"  Password Strength:  {strength}")
    print("=" * 45)

    # Option to generate another
    while get_yes_no("\nGenerate another password with the same settings? (y/n): "):
        password = generate_password(length, use_uppercase, use_digits, use_symbols)
        print("\n" + "=" * 45)
        print(f"  Generated Password:  {password}")
        print("=" * 45)

    print("\n✅ Goodbye! Keep your passwords safe.")


if __name__ == "__main__":
    main()
