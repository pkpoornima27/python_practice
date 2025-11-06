""" 8. Convert Celsius to Fahrenheit"""

### F = (C * 9/5) + 32

c_temp = int(input("Enter the temp in celsius"))

def convert_fahrenheit(temp):
    f_temp = (temp * 9/5) + 32
    return f_temp

print(c_temp)
print(convert_fahrenheit(c_temp))