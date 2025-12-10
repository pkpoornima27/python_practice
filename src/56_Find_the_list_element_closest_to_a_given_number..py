""" 56. Find the list element closest to a given number."""

l1 = [2, 5, 8, 9, 10, 11, 12, 14, 27]
user_num = int(input("Enter the number"))

def find_num_close_to_user_num(test_list, num):
    print(test_list)
    print(num)
    diff_dict = {}
    for element in test_list:
        diff = abs(element - num)
        diff_dict[element] = diff
    print(diff_dict)
    min_diff = min(diff_dict, key= diff_dict.get)
    return min_diff

closest_num = find_num_close_to_user_num(l1, user_num)
print(f"Closest Number:{closest_num}")
