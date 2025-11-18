""" 48. Find common elements between two lists"""

l1 = [1, 2, 3, 4, 5]
l2 = [2, 3, 4, 5, 6]

print("first list:", l1)
print("second list:", l2)

def common_elements(list_l1, list_l2):
    common_list = []
    for x in list_l1:
        if x in list_l2:
            common_list.append(x)
    return common_list

print("Common elements in two lists:", common_elements(l1, l2))

#using list comprehension
common = [x for x in l1 if x in l2]
print("Common elements in two lists using list comprehension:", common)
