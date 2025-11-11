""" 25. Count the number of words in a sentence"""
user_str = input("Enter the string:")

def count_word(s):
    print(s)
    str_lst = s.split()
    print(str_lst)
    return len(str_lst)


print(count_word(user_str))