""" 51. Find the average of list elements"""


l_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def list_average(l):
    print(l)
    if not l:
        return 0
    return sum(l) /len(l)

print("Average of all elements in the list:", list_average(l_list))