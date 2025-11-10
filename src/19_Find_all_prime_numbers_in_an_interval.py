""" 19. Find all prime numbers in an interval"""

start = int(input("Enter the beginning of the interval"))
end = int(input("Enter the end of the interval"))

print(f"The prime numbers between {start} and {end} of the interval:")

for num in range(start, end+1):
    if num > 1:
        for i in range(2, num):
            if num%i == 0:
                break
        else:
            print(num)