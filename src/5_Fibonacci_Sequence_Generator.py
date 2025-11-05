#Prints the fibonacci series

num = int(input("enter the number:"))
num1 = 0
num2 = 1
print(num1)
print(num2)
total = 0
for i in range(2, num):
    total = num1 + num2
    print(total)
    num1 = num2
    num2 = total
