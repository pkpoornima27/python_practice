##9. Armstrong Number Checker

num = int(input("Enter the number:"))
print(num, "entered the number")

sum = 0
temp = num

while temp>0:
    digit = temp % 10
    #print(digit)
    sum = sum + digit ** 3
    temp = temp//10

print("*********")
if sum == num:
    print(num, "Is the Armstrong Number")
else:
    print(num, "is the ")