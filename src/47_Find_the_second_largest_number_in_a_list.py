""" 47. Find the second-largest number in a list"""

l1 = [4, 6, 2, 7, 1, 8, 0, 4, 6, 2, 7, 1]
print(l1)

def second_largest_manually(list_l):
    copy_list = list_l[:]
    list_length = len(copy_list)
    for i in range(0, list_length):
        for j in range(i+1, list_length):
            if copy_list[i] > copy_list[j]:
                copy_list[i], copy_list[j] = copy_list[j], copy_list[i]
    print(copy_list)
    return copy_list[-2]

print("Second largest in list:", second_largest_manually(l1))

l1.sort()
print("Second largest using sort function:", l1[-2])