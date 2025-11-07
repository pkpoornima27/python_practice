"""11. Calculate the factorial of a number"""


num = int(input("enter the number"))

def factorial(n):
    fact = 1
    while n > 0:
        fact = fact * n
        n -= 1
    return fact

print(factorial(num))