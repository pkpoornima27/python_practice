""" 30. Check if two strings are anagrams"""

str1 = input("Enter the first string")
str2 = input("Enter the second string")

def check_anagram(s1, s2):
    print(s1)
    print(s2)
    if sorted(s1) == sorted(s2):
        print(f"{s1} and {s2} are anagram")
    else:
        print(f"{s1} and {s2} are not anagram")


check_anagram(str1, str2)