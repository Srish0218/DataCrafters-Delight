"""
Factorial program in c using command line arguments.
Explanation: Factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less
than or equal to n. For example, The value of 5! is 5*4*3*2*1 = 120
"""
def get_fact(num):
    fact = 1
    for i in range(1 , num +1):
        fact = fact * i
    print(fact)


num = int(input("Num: "))
get_fact(num)