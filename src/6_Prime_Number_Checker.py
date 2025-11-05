##User enters the number and this program checks if the number is prime number or not

num = int(input("Enter the number:"))
flag = False
if num == 0 and num == 1:
    print("Its not prime number")
elif num>1:
    for i in range(2, num):
        if num%i == 0:
            flag = True
            break

if flag:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")