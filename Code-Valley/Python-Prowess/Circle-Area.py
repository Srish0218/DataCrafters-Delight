"""

Write a  program, to find the area of a circle when the diameter is given. The
input diameter is an integer and the output area should be a floating point
variable with 2 point precision.

"""
import math

def find_area(r):
    area = math.pi * (r**2)
    print("{:.2f}".format(area))

diameter = int(input("Diameter: "))
find_area(diameter / 2)
