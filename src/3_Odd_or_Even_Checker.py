##This program checks if user entered number is even of odd

num = int(input("Enter a number:"))
remainder = num%2
if remainder == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")