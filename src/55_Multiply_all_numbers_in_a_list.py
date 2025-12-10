""" 55. Multiply all numbers in a list """

test_list = [2, 5, 8, 2, 9, 10, 11, 12, 14, 27, 5, 2]
product = 1
for element in test_list:
    product *= element
print(f"Product of all elements of the list: {product}")