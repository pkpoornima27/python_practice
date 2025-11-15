""" 38. Split and join a string."""

str_lst = input("enter the list of the character to be joined")

def split_join_string(s):
    print(s)
    words = s.split()
    print(words)
    join_str = '-'.join(words)
    print(join_str)

split_join_string(str_lst)