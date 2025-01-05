import pyfiglet
from termcolor import colored

def display_banner():
    # Using 'starwars' font for a more hacking-like appearance (you can experiment with other fonts too)
    banner_tool = pyfiglet.figlet_format("Password Strength Checker", font="starwars")
    banner_by = pyfiglet.figlet_format("By LIX Hack", font="starwars")
    print(colored(banner_tool, "green"))
    print(colored(banner_by, "red"))
    print()

def check_password_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)
    score = 0
    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1
    if score <= 2:
        return "Weak", "red"
    elif score == 3:
        return "Moderate", "yellow"
    else:
        return "Strong", "green"

def main():
    display_banner()
    password = input(colored("Enter a password to check its strength: ", "cyan"))
    strength, color = check_password_strength(password)
    print(colored(f"Password Strength: {strength}", color))

if __name__ == "__main__":
    main()
