""" 34. Find the most frequent character"""
user_str = input("Enter the string")

def frequent_character(s):
    print(s)
    freq = {}
    #count freq of characters
    for element in s:
        freq[element] = freq.get(element, 0) + 1

    #max
    max_char  = max(freq, key = freq.get)
    return max_char, freq[max_char]

char, count = frequent_character(user_str)
print(f"the most freq character is {char} and it appeared {count} times")
