""" 43. Remove duplicates from a list"""

l1 = [4, 6, 2, 7, 1, 8, 0, 4, 6, 2, 7, 1]
print(l1)
print("After removing the duplicate elements from list")
print(list(set(l1)))

def remove_duplicate(l_list):
    seen = set()
    duplicate = []
    for i in l_list:
        if i not in seen:
            seen.add(i)
            duplicate.append(i)
    return duplicate

dup_list =  remove_duplicate(l1)
print(f"After removing all the duplicate items from {l1}: {dup_list}")
