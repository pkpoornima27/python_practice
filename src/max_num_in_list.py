li = [29, 4, 59, 99, 73, 28, 67, 9]
max = li[0]
for num in li:
    if max < num:
        max = num

print(max)

min = li[0]
for num in li:
    if min > num:
        min = num
print(min)