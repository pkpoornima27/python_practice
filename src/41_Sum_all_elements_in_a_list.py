""" 41. Sum all elements in a list"""
l1 = [4, 6, 2, 7, 1, 8, 0, 4]

def sum_of_list(l):
    total = 0
    for num in l:
        total += num
    return total

result = sum_of_list(l1)
print("Sum using loop:", result)
print("Sum using sum():", sum(l1))