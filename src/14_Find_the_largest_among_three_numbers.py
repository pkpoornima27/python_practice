""" 14. Find the largest among three numbers"""
##
num_list = []
for i in range(1, 4):
    n = int(input("Enter the number"))
    num_list.append(n)
print(num_list)
largest = max(num_list)
print(f"{largest} is the largest of all three entries")
