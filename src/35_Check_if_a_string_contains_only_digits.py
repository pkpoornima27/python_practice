""" 35. Check if a string contains only digits"""

user_str = input("Enter the string: ")

def check_only_digit(s):
    print(s)
    for char in s:
        if not char.isdigit():
            return False
    return True

if check_only_digit(user_str):
    print(f"{user_str} has only digits")
else:
    print(f"{user_str} has other characters")

