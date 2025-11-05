""" User enters 2 strings and function is to find out the common characters"""

def common_char(str):
    print(str)
    s = set(str)
    return s

str1 = input("enter first string")
str2 = input("enter second string")

s1 = common_char(str1)
s2 = common_char(str2)

common_letters = s1 & s2
print(common_letters)


