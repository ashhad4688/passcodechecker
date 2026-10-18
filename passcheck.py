import re

def check_password_strength(password):
    # Check length and character criteria
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Score calculation based on passed criteria
    score = 5 - sum([length_error, digit_error, uppercase_error, lowercase_error, symbol_error])

    if score == 5:
        return "Strong Password"
    elif score >= 3:
        return "Moderate Password"
    else:
        return "Weak Password"

if __name__ == "__main__":
    pwd = input("Enter password to evaluate: ")
    print(f"Strength Rating: {check_password_strength(pwd)}")