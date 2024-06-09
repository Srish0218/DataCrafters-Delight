"""

Write a program, to check whether the given year is a leap year or not. A leap
year is a calendar year containing one additional day(Feb 29th)added to keep the
calendar year synchronized with the astronomical year.


Here's a breakdown of the conditions:

If the year is not divisible by 4, it's not a leap year.
If the year is divisible by 4 but not by 100, it's a leap year.
If the year is divisible by 100 and also by 400, it's a leap year.

"""


def is_leap_year(year):

    if year % 4 != 0:
        return False

    if year % 100 == 0 and year % 400 != 0:
        return False

    return True


# Example usage:

year = int(input("Year: "))

if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
