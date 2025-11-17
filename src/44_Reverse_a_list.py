""" 44. Reverse a list"""

l1 = [4, 6, 2, 7, 1, 8, 0, 4]
print(l1)

def reverse_list_builtin(l_list):
    reverse = []
    size = len(l_list)
    for i in range(size-1, -1, -1 ):
        reverse.append(l_list[i])
    return reverse

print("Reversed list:", reverse_list_builtin(l1))
l1.reverse()
print("Reversed list using built in function:", l1)






