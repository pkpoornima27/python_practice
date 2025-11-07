"""  12. Generate multiplication table."""

num = int(input("Enter the number"))
print(f"{num} times table")
for i in range(1, 11):
    product = num * i
    print(f"{num} X {i} = {product}")

