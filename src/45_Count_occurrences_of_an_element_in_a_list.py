""" 45. Count occurrences of an element in a list"""

l1 = [4, 6, 2, 7, 1, 8, 0, 4, 6, 2, 1]
print(l1)
element = int(input("enter the element"))

def count_occurrence(full_list, ele):
    count = 0
    for i in full_list:
        if i == ele:
            count +=1
    return count

print(f"{element} occurred {count_occurrence(l1, element)} times")