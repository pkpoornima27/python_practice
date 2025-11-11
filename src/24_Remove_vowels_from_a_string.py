"""" 24. Remove vowels from a string"""
user_str = input("enter the string")

def remove_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    no_vowels = ""
    for char in s:
        if char.lower() not in vowels:
            no_vowels = no_vowels + char

    return no_vowels


print(remove_vowels(user_str))