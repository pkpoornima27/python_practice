""" 23. Count vowels and consonants in a string"""
user_str = input("Enter the string:")

def count_vowels_consonants(s):
    vowels = 0
    consonants = 0
    lower_s = s.lower()
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    for char in lower_s:
        if char.isalpha():
            if char in vowels_list:
                vowels +=1
            else:
                consonants +=1
    print(f"Vowels count: {vowels}")
    print(f"Consonants count: {consonants}")

count_vowels_consonants(user_str)