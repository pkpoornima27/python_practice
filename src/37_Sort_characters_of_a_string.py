""" 37. Sort characters of a string"""

user_str = input("Enter the string")

def sort_string(s):
    print(s)
    return ''.join(sorted(s))

print("Sorted string:", sort_string(user_str))