"""  53. Find duplicates in a list. """


l1 = [2, 5, 8, 2, 9, 10, 11, 12, 14, 27, 5, 2]

def find_duplicate(list_x):
    duplicate_list = []
    for element in list_x:
        count = list_x.count(element)
        if count > 1:
            duplicate_list.append(element)
    return set(duplicate_list)

print(f"The duplicate elements in the list are:{find_duplicate(l1)}")