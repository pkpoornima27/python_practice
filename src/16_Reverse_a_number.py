""" 16. Reverse a number"""

num = 987654321
reverse = 0
while num != 0:
     rem = num % 10
     reverse = reverse * 10 + rem
     num = num // 10
print(reverse)
