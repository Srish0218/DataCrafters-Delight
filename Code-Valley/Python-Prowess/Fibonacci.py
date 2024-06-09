"""

Consider the below series:
1, 2, 1, 3, 2, 5, 3, 7, 5, 11, 8, 13, 13, 17, ...
This series is a mixture of 2 series – all the odd terms in this series form a Fibonacci series and all the even
terms are the prime numbers in ascending order.
Write a program to find the Nth term in this series.
The value N is a Positive integer that should be read from STDIN. The Nth term that is calculated by the
program should be written to STDOU2T. Other than the value of Nth term, no other characters/strings or
message should be written to STDOUT.
For example, when N = 14, the 14th term in the series is 17. So only the value 17 should be printed to
STDOUT.

def fibonacci(n):
    t1, t2 = 0, 1
    for _ in range(1, n + 1):
        print(t1, end=" , ")
        next_term = t1 + t2
        t1 = t2
        t2 = next_term


num = int(input("Num: "))
fibonacci(num)

"""


def fibonacci(n):
    t1, t2 = 0, 1
    for _ in range(1, n + 1):
        next_term = t1 + t2
        t1 = t2
        t2 = next_term
    print(t1)


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime(n):
    count = 0
    for i in range(2, 1000):
        if is_prime(i):
            count += 1
        if count == n:
            print(i)
            break


n = int(input())
if n % 2 == 1:
    fibonacci((n // 2) + 1)
else:
    prime(n // 2)
