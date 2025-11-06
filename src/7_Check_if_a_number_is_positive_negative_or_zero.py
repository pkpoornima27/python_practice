""" 7. Check if a number is positive, negative, or zero"""
num = int(input("Enter the number:"))

def num_check(n):
    if n > 0:
        print(f"{n} is the positive number")
    elif n < 0:
        print(f"{n} is the negative number")
    else:
        print(f"{n} is a zero")

num_check(num)