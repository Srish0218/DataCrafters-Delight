"""
## Selection Sort Algorithm
Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list.

### How it Works
1. **Initialization**:
   - Start with the entire sorted list.
   - Define two pointers: `start` and `end`, initially pointing to the first and last elements of the list respectively.

2. **Finding the Minimum Element**:
   - Iterate over the unsorted portion of the list to find the minimum element.
   - Swap the minimum element with the first element of the unsorted portion.

3. **Repeat**:
   - Repeat the process for the remaining unsorted portion until the entire list is sorted.

### Example
Consider an array `arr[] = {64, 25, 12, 22, 11}`.

#### Passes:
1. **First Pass**: Swap the first element with the minimum in the array.
2. **Second Pass**: Swap the second element with the next minimum element.
3. **Third Pass**: Swap the third element with the next minimum element.
4. **Fourth Pass**: Swap the fourth element with the next minimum element.
5. **Fifth Pass**: The largest value automatically gets placed at the last position.


### Complexity Analysis
- **Time Complexity**: O(N^2)
- **Space Complexity**: O(1)

### Advantages
- Simple and easy to understand.
- Works well with small datasets.

### Disadvantages
- Time complexity of O(N^2) in the worst and average case.
- Does not work well on large datasets.
- Not stable.

### FAQs
1. **Is Selection Sort Algorithm stable?**
   - By default, it's not stable, but it can be made stable.

2. **Is Selection Sort Algorithm in-place?**
   - Yes, it's an in-place algorithm.
"""


def Selection_Sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr


li = [int(x) for x in input("Enter elements (separated by spaces): ").split()]
result = Selection_Sort(li)
print(result)
