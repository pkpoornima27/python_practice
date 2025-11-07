""" 13. Generate Fibonacci series up to n terms."""

num = int(input("Enter the number"))
first_num = 0
second_num = 1

print(first_num)
print(second_num)
for i in range(1, num+1):
    total = first_num + second_num
    print(total)
    first_num = second_num
    second_num = total

