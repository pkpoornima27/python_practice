""" 31. Find duplicate characters in a string"""

user_str = input("Enter the string")

def duplicate_char(s):
    print(s)
    duplicate_character = []
    for element in s:
        if s.count(element) > 1:
            if element not in duplicate_character:
                duplicate_character.append(element)
    return duplicate_character

print(duplicate_char(user_str))