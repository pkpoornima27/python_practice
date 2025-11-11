""" 27. Remove punctuation from a string"""

import string
user_str = input("Enter the string")

def remove_punctuation(s):
    print(s)
    new_str = ""
    for char in s:
        if char not in string.punctuation:
            new_str = new_str + char
    print(new_str)

remove_punctuation(user_str)