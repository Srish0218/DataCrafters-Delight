"""
Binary Search is defined as a searching algorithm used in a sorted array by repeatedly dividing the search
interval in half. The idea of binary search is to use the information that the array is sorted and reduce the time
complexity to O(log N).

Conditions for when to apply Binary Search in a Data Structure:
- To apply Binary Search algorithm:
- The data structure must be sorted.
- Access to any element of the data structure takes constant time.

Binary Search Algorithm: - Divide the search space into two halves by finding the middle index “mid”. Finding the
middle index “mid” in Binary Search Algorithm - Compare the middle element of the search space with the key. - If the
key is found at middle element, the process is terminated. - If the key is not found at middle element, choose which
half will be used as the next search space. - If the key is smaller than the middle element, then the left side is
used for next search. - If the key is larger than the middle element, then the right side is used for next search. -
This process is continued until the key is found or the total search space is exhausted. - This code implements the
binary search algorithm to find a target element `k` within a sorted list `arr`. Let's dissect it:

1. **Function Definition**:
    ```python
    def Binary_Search(arr, k):
    ```
   This defines a function named `Binary_Search` which takes two arguments:
   - `arr`: the sorted list in which the search will be performed.
   - `k`: the target element to search for in the list.

2. **Initialization**: ```python start = 0 end = len(arr) - 1 mid = start + (end - start) // 2 ``` Here, `start` is
initialized to the beginning of the list (`0`), `end` is initialized to the last index of the list (`len(arr) - 1`),
and `mid` is calculated as the middle index of the list.

3. **Binary Search Loop**:
    ```python
    while start <= end:
    ```
   This initiates a `while` loop that continues as long as the `start` index is less than or equal to the `end` index.

4. **Middle Element Check**: ```python if arr[mid] == k: return mid ``` If the middle element `arr[mid]` is equal to
the target element `k`, it means we have found the element, so the index `mid` is returned.

5. **Adjusting Search Range**: ```python elif arr[mid] > k: end = mid - 1 elif arr[mid] < k: start = mid + 1 ``` If
the middle element is greater than `k`, it means the target lies in the left half of the list, so we update the `end`
index to `mid - 1`. If the middle element is less than `k`, it means the target lies in the right half of the list,
so we update the `start` index to `mid + 1`.

6. **Updating Middle Index**:
    ```python
    mid = start + (end - start) // 2
    ```
   After adjusting the search range, the middle index is updated accordingly.

7. **Return "Not Found"**: ```python return "Not Found" ``` If the loop exits without finding the element,
it means the element is not present in the list, so "Not Found" is returned.

8. **User Input and Function Call**: ```python li = [int(x) for x in input("Enter elements in list (separated by
spaces): ").split()] key = int(input("Enter element to Search: ")) result = Binary_Search(li, key) ``` Here,
the user is prompted to input the elements of the list and the element to search for. Then, the `Binary_Search`
function is called with the list `li` and the target element `key`.

9. **Printing Result**:
    ```python
    print("Element Found at index: ", result)
    ```
   Finally, the result of the search is printed to the console.

This code efficiently searches for an element in a sorted list using the binary search algorithm. If the element is
found, it returns the index where it is located; otherwise, it returns "Not Found"."""


def Binary_Search(arr, k):
    start = 0
    end = len(arr) - 1
    mid = start + (end - start) // 2
    while start <= end:
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            end = mid - 1
        elif arr[mid] < k:
            start = mid + 1
        mid = start + (end - start) // 2
    return "Not Found"


li = [int(x) for x in input("Enter elements in list (separated by spaces: ").split()]
key = int(input("Enter element to Search: "))
result = Binary_Search(li, key)
print("Element Found at index: ", result)
