""" 17. Check if a number is palindrome """

num = int(input("enter the number"))

def reverese_number(n):
    rev = 0
    while n!=0:
        r = n % 10
        rev = rev * 10 + r
        n = n // 10
    return rev

reverse = reverese_number(num)
if num == reverse:
    print(f"{num} is paliandrome")
else:
    print(f"{num} is not paliandrome")