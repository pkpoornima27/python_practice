""" 3. Swap two numbers. """
"""3_Swap_two_numbers"""

num1 = int(input("Enter first num"))
num2 = int(input("Enter second number"))

def swap_num(n1, n2):
    n1, n2 = n2, n1
    print("after swapping")
    print("the first number:", n1)
    print("the second number:", n2)

swap_num(num1, num2)