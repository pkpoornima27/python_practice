""" 26. Convert string to uppercase/lowercase"""

user_str = input("enter the string")

def convert_lower_upper(s):
    print(s)
    print(s.swapcase())
    print(s.upper())
    print(s.lower())

convert_lower_upper(user_str)