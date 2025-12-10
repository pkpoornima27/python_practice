"""  54. Remove all zeros from a list. """

l1 = [2, 0, 5, 8, 2, 9, 10, 0, 11, 12, 14, 0, 27, 5, 2]
print(l1)
non_zero_list = [x for x in l1 if x != 0]
print(non_zero_list)