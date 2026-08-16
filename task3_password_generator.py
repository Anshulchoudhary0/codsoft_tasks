import random
import string


def generate_password(
    length, use_upper=True, use_digits=True, use_symbols=True
):
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        return "Error: No character types selected."

    return "".join(random.choice(chars) for _ in range(length))


def main():
    print("=== Random Password Generator ===")
    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print("Length must be a positive integer.")
            return

        use_upper = (
            input("Include uppercase letters? (y/n): ").strip().lower() == "y"
        )
        use_digits = input("Include numbers? (y/n): ").strip().lower() == "y"
        use_symbols = (
            input("Include special characters? (y/n): ").strip().lower() == "y"
        )

        password = generate_password(
            length, use_upper, use_digits, use_symbols
        )
        print(f"\nGenerated Password: {password}")
    except ValueError:
        print("Invalid input! Please enter a valid number for length.")


if __name__ == "__main__":
    main()
