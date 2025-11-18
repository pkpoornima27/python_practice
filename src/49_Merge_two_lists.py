""" 49. Merge two lists"""


l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]

full_list = [x for x in l1] + [y for y in l2]
print("Merged list:", full_list)