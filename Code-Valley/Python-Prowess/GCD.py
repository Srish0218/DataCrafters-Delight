"""
find the GCD of the given 2 numbers, using command line arguments. The input is 2
integer and the output GCD also should be an integer value.
"""

import sys


def gcd(a, b):
    while b != 0:
        # print(f"Before logic: {a}   {b}")
        a, b = b, a % b
        # print(f"After logic: {a}   {b}")
        #
        # if b==0:
        #     print("B is 0 now!!!!!!!")
    return a


num1 = int(input("NUm1: "))
num2 = int(input("Num2: "))

# Calculate and print the GCD
print("The GCD of", num1, "and", num2, "is:", gcd(num1, num2))
