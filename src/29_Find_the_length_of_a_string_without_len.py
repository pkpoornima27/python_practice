""" 29. Find the length of a string (without len())"""

user_str = input("Enter the string")

def string_len(s):
    print(s)
    count = 0
    for char in s:
        count += 1
    return count

print(f"Length of the string entered:", string_len(user_str))