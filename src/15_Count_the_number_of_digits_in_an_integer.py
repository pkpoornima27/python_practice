""" 15. Count the number of digits in an integer"""

num = 34527587658765
count = 0

while num != 0:
    num //= 10
    count += 1

print(f"The digit count: {count}")


