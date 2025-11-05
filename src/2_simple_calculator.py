##Simple Calculator
##This program allows the user to enter 2 numbers and the math operator

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
sign = input("Enter the Math operator:")
print(num1, num2, sign)

if sign == '+':
    sum = num1+num2
    print("Sum of", num1, "and", num2, "equals", sum)
elif sign == '-':
    diff = num1-num2
    print("Difference between", num1, "and", num2, "equals", diff)
elif sign == "*":
    mul = num1*num2
    print("Multiplication", mul)
elif sign == "/":
    div = num1/num2
    print("Division", div)
else:
    print("User entered sign is not math operator")