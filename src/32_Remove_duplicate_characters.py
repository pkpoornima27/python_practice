"""  32. Remove duplicate characters"""
user_str = input("Enter the string")

def remove_duplicate_char(s):
    print(s)
    seen = set()
    new_str = ""
    for char in s:
        if char not in seen:
            seen.add(char)
            new_str = new_str + char
    return new_str

print("The updated string without duplicate characters:", remove_duplicate_char(user_str))