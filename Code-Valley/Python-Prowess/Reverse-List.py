"""
Approach 1
Sure, let's break down the logic of the `reverse` function step by step:

1. **Function Definition**:
    ```python
    def reverse(li):
    ```
   This line defines a function named `reverse` that takes a single argument `li`, which is expected to be a list.

2. **Finding Length of List**: ```python length = len(li) ``` Here, the `len()` function is used to find the length
of the input list `li` and store it in the variable `length`. This will be used later to determine the number of
iterations required to reverse the list.

3. **Reversing the List**: ```python for i in range(length // 2): ``` This line initiates a `for` loop that iterates
over half of the length of the list. Since we're swapping elements from both ends simultaneously, we only need to
iterate till halfway through the list.

4. **Swapping Elements**: ```python li[i], li[length - i - 1] = li[length - i - 1], li[i] ``` Inside the loop,
this line swaps the elements at indices `i` and `length - i - 1`. - `li[i]` represents the element at the `i`-th
position from the start of the list. - `li[length - i - 1]` represents the element at the position equivalent to `i`
from the end of the list. This is how we access elements from the end of the list. - By swapping these two elements,
we effectively reverse the list. - The swapping is done using Python's simultaneous assignment feature.

5. **Function Execution**: ```python li = [1, 2, 3, 4, 5] reverse(li) ``` Here, we create a list `li` with elements
`[1, 2, 3, 4, 5]`, and then call the `reverse` function passing this list as an argument. This will reverse the list
`li` in place.

6. **Printing the Result**:
    ```python
    print(li)
    ```
   Finally, we print the reversed list `li` after calling the `reverse` function.

So, when you run this code, you'll get the reversed list printed: `[5, 4, 3, 2, 1]`.
"""


def reverse1(li):
    length = len(li)
    for i in range(length // 2):
        li[i], li[length - i - 1] = li[length - i - 1], li[i]


li = [1, 2, 3, 4, 5]
reverse1(li)
print("Using Approach 1: ", li)

"""
Approach 2:

The `reverse2` function follows a similar approach to reverse the list as the previous function, but with a slight 
difference in how it accesses elements from the end of the list. Let's break it down:

1. **Function Definition**: 
    ```python
    def reverse2(li):
    ```
   This line defines a function named `reverse2` that takes a single argument `li`, which is expected to be a list.

2. **Reversing the List**:
    ```python
    for i in range(len(li) // 2):
    ```
   This line initiates a `for` loop that iterates over half of the length of the list, similar to the previous function.

3. **Swapping Elements**: ```python li[i], li[- i - 1] = li[- i - 1], li[i] ``` Inside the loop, this line swaps the 
elements at indices `i` and `-i-1`. - `li[i]` represents the element at the `i`-th position from the start of the 
list. - `li[-i-1]` represents the element at the position equivalent to `i` from the end of the list. `-i-1` is used 
to access elements from the end of the list. - By swapping these two elements, we effectively reverse the list.

4. **Function Execution**: ```python li2 = [1, 2, 3, 4, 5] reverse2(li2) ``` Here, we create a list `li2` with 
elements `[1, 2, 3, 4, 5]`, and then call the `reverse2` function passing this list as an argument. This will reverse 
the list `li2` in place.

5. **Printing the Result**:
    ```python
    print("Using Approach 2: ", li2)
    ```
   Finally, we print the reversed list `li2` after calling the `reverse2` function. 

Both approaches achieve the same result: reversing the list. The second approach simply accesses elements from the 
end of the list using negative indices, which makes the code a bit more concise. When you run this code, you'll get 
the reversed list printed as expected.

"""


def reverse2(li2):
    for i in range(len(li2) // 2):
        li2[i], li2[- i - 1] = li2[- i - 1], li2[i]


li2 = [1, 2, 3, 4, 5]
reverse2(li2)
print("Using Approach 2: ", li2)

"""
Approach 3(most simple):

This code snippet reverses the list `li` using Python's slice notation and then prints the reversed list. Let's break 
it down:

1. **List Reversal**: ```python var = li[::-1] ``` Here, `li[::-1]` creates a new list containing all elements of 
`li` in reverse order. - The slice notation `[::-1]` means "start from the end, go all the way to the beginning, 
and take steps of -1", effectively reversing the list.

2. **Variable Assignment**:
    ```python
    var = li[::-1]
    ```
   The reversed list is assigned to the variable `var`.

3. **Printing the Reversed List**:
    ```python
    print(var)
    ```
   Finally, the reversed list stored in `var` is printed to the console.

So, when you run this code snippet, it will print the reversed list `[5, 4, 3, 2, 1]`. This approach creates a new 
list with the reversed elements, leaving the original list `li` unchanged."""

li = [1, 2, 3, 4, 5]
var = li[::-1]
print("Using Approach 3: ", var)

