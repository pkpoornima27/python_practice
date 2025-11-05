for row in range(0, 5):
    for col in range(0, 5):
        print("*", end= " ")
    print()

print()
print()

sum = 0
for row in range(1, 6):
    for col in range(1, 6):
        sum = sum + 1
        print(sum, end= " ")
    print()

for row in range(0, 5):
    for col in range(0, row+1):
        print("*", end= " ")
    print()

print()

for row in range(5, 0, -1):
    for col in range (0, row):
        print("*", end= " ")
    print()

print()

for row in range(0, 7, 2):
    for col in range(0, row+1):
        print("*", end= " ")
    print()
print()

num = 5
for row in range(1, num+1):
    for col in range(1, num-row+1):
        print(end= " ")
    for col in range(1, row+1):
        print("*", end=" ")
    print()

print()

num1 = 5
for row in range(num1, 0, -1):
    for col in range(1, row-num1+1):
        print(end= " ")
    for col in range(1, row+1):
        print("*", end= " ")
    print()