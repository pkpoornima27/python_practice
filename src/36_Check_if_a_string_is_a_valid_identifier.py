"""36. Check if a string is a valid identifier"""

import keyword
user_str = input("Enter the string")
if user_str.isidentifier() and keyword.iskeyword(user_str):
    print(f"{user_str} is a valid identifier")
else:
    print(f"{user_str} is not valid identifier")