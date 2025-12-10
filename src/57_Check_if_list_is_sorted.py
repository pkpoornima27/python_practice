"""   57. Check if list is sorted."""

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [2, 4, 7, 3, 1, 5, 5, 9, 8]

def check_list_sorted(test_l):
    return test_l ==  sorted(test_l)

for lst in [l1, l2]:
    status = check_list_sorted(lst)
    print(f"{lst} is {status} sorted list")


