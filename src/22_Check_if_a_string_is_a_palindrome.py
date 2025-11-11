""" 22. Check if a string is a palindrome"""

usr_str = input("enter the string:")

def check_palindrome(s):
    print(s)
    rev = ""
    for char in s:
        rev = char + rev
    print(rev)
    if s == rev:
        print(f"{s} is a palindrome")
    else:
        print(f"{s} is not a palindrome")

check_palindrome(usr_str)