""" 50. Separate even and odd numbers in a list"""

l_list = [2, 5, 8, 3, 8, 9, 1, 7]

even_list = [x for x in l_list if x%2 == 0]
odd_list = [y for y in l_list if y%2 != 0]
print("Even list:", even_list)
print("Odd List:", odd_list)