""" 28. Replace a substring in a string"""

user_str = input("Enter the string")
replaced_str = input("Enter the string to be replaced")
new_str = input("Enter the new string")

def substring_replace(s, rep, new):
    print("Original String", s)
    updated_string =  s.replace(rep, new)
    return updated_string


print("Replaced string:", substring_replace(user_str, replaced_str, new_str))

