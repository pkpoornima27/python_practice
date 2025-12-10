""" 58. Flatten a nested list"""

test_list1 = [2, 4, 5, [8, 6, 7], [9, 11, 15]]
test_list2 = [1, [2, [3, [4, 1, 2], 5], 6]]

def flat_list(l1):
    result = []
    for ele in l1:
        if isinstance(ele, list):
            result.extend(flat_list(ele))
        else:
            result.append(ele)
    return result

print(flat_list(test_list1))
print(flat_list(test_list2))