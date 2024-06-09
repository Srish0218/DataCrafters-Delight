"""
Calculate length of hypotenuse of right-angled triangle
"""
from math import sqrt


# def sqrt(x):
#     if x == 0:
#         return 0
#     guess = x
#     while True:
#         new_guess = 0.5 * (guess + x / guess)
#         if abs(new_guess - guess) < 0.00001:
#             return new_guess
#         guess = new_guess

def hypotenuse_length(a, b):
    return sqrt(a ** 2 + b ** 2)


# Example usage:
a = float(input("Enter the length of side 'a': "))
b = float(input("Enter the length of side 'b': "))

hypotenuse = hypotenuse_length(a, b)
print("Length of hypotenuse:", hypotenuse)
