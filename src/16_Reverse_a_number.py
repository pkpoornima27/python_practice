""" 16. Reverse a number"""

num = 987654321
reverse = " "
while num != 0:
     rem = num % 10
     reverse = reverse + str(rem)
     num = num // 10
print(int(reverse))
