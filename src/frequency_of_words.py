""" Example: Sheena loves eating apple and mango. And her sister also loves eating apple and mango"""

def freq_words():
    str=input("Enter the string")
    li = str.split()
    print(li)
    d = {}

    for i in li:
        if i not in d.keys():
            d[i] = 0
        d[i] = d[i]+1
    print(d)
freq_words()