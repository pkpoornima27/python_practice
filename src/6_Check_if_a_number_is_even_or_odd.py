""" 6. Check if a number is even or odd"""

number = int(input("Enter the number:"))

def check_even_odd(num):
    if num%2 == 0:
        print(f"{num} is the even number")
    else:
        print(f"{num} is the odd number")

check_even_odd(number)
