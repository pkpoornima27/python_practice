""" 42. Find the maximum and minimum in a list"""

l1 = [4, 6, 2, 7, 1, 8, 0, 4]

def min_max(l):
    min_element = min(l)
    max_element = max(l)
    return min_element, max_element

min_m, max_m = min_max(l1)
print(f"From list {l1}, minimum element: {min_m} and maximum element: {max_m}")