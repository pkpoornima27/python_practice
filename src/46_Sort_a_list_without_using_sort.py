""" 46. Sort a list without using sort()"""

l1 = [4, 6, 2, 7, 1, 8, 0, 4, 6, 2, 7, 1]
print(l1)

def sort_manually(list_l):
    length = len(list_l)
    for i in range(0, length):
        for j in range(i+1, length):
            if list_l[i] > list_l[j]:
                list_l[i], list_l[j] = list_l[j], list_l[i]
    return list_l

print("Sorting manually:", sort_manually(l1))
l1.sort()
print("Sorting using function", l1)