""" 18. Check if a number is prime."""
num = int(input("Enter the number"))

def prime_check(n):
    if n<=1:
        return False
    for i in range(2, n+1):
        if n%i == 0:
            return False
        else:
            return True

flag = prime_check(num)
if flag == True:
    print(f"{num} is a Prime number")
else:
    print(f"{num} is not a Prime number")