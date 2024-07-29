import re

def check_password_complexity(password):
    """
    Check if the given password meets the complexity requirements.

    :param password: The password string to check.
    :return: A tuple containing a boolean result and a list of reasons why the password is invalid (if any).
    """
    # Define complexity requirements
    min_length = 8
    max_length = 20
    special_characters = re.compile(r'[!@#$%^&*(),.?":{}|<>]')
    upper_case = re.compile(r'[A-Z]')
    lower_case = re.compile(r'[a-z]')
    digits = re.compile(r'[0-9]')

    reasons = []
    is_valid = True

    # Check length
    if len(password) < min_length:
        is_valid = False
        reasons.append(f"Password must be at least {min_length} characters long.")
    if len(password) > max_length:
        is_valid = False
        reasons.append(f"Password must be no more than {max_length} characters long.")

    # Check for uppercase letters
    if not upper_case.search(password):
        is_valid = False
        reasons.append("Password must contain at least one uppercase letter.")

    # Check for lowercase letters
    if not lower_case.search(password):
        is_valid = False
        reasons.append("Password must contain at least one lowercase letter.")

    # Check for digits
    if not digits.search(password):
        is_valid = False
        reasons.append("Password must contain at least one digit.")

    # Check for special characters
    if not special_characters.search(password):
        is_valid = False
        reasons.append("Password must contain at least one special character.")

    return is_valid, reasons

def main():
    # Prompt user for input
    password = input("Enter a password to check: ")
    
    # Check the complexity of the entered password
    is_valid, reasons = check_password_complexity(password)

    # Provide feedback to the user
    if is_valid:
        print("Password is valid.")
    else:
        print("Password is invalid:")
        for reason in reasons:
            print(f"- {reason}")

if __name__ == "__main__":
    main()
