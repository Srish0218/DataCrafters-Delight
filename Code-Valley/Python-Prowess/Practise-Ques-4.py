# Samjh ni aya


"""
Problem Statement –

Joseph is learning digital logic subject which will be for his next semester. He usually tries to solve unit
assignment problems before the lecture. Today he got one tricky question. The problem statement is “A positive
integer has been given as an input. Convert decimal value to binary representation. Toggle all bits of it after the
most significant bit including the most significant bit. Print the positive integer value after toggling all bits”.
"""

# def toggle_bits(n):
#     # Convert the decimal number to binary representation
#     binary = bin(n)[2:]  # Convert to binary and remove '0b' prefix
#
#     # Toggle all bits after the most significant bit (MSB)
#     toggled_binary = ''.join(['1' if bit == '0' else '0' for bit in binary])
#
#     # Convert the toggled binary representation back to decimal
#     result = int(toggled_binary, 2)
#
#     return result
#
# # Test the function with an example
# decimal_input = 111
# result = toggle_bits(decimal_input)
# print("Result after toggling bits:", result)

import math
n=int(input())
k=(1<< int(math.log2(n))+1)-1
print(n^k)