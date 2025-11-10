""" 21. Reverse a string"""

usr_str = input("enter the string")

def string_reverse(s):
    rev = ""
    for char in s:
        rev = char + rev
    return rev

print("String reversed:")
print(string_reverse(usr_str))