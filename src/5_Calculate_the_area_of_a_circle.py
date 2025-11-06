""" 5. Calculate the area of a circle"""
""" area = pi * radius^2"""
import math

radius = int(input("Enter the radius"))

def circle_ares(r):
    area = math.pi * (r ** 2)
    return area
print("Area of the circle:")
print(circle_ares(radius))