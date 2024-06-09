"""## Bubble Sort Algorithm
Bubble sort is a simple sorting algorithm that works by repeatedly swapping adjacent
elements if they are in the wrong order. Although simple, it is not efficient for large datasets due to its high time
complexity.

### How it Works
1. **Initialization**:
   - Start from the beginning of the array.
   - Traverse the array and compare adjacent elements.

2. **Sorting Process**:
   - If the elements are in the wrong order (i.e., the current element is greater than the next one), swap them.
   - Move to the next pair of elements and repeat the comparison and swapping process until the entire array is sorted.

3. **Passes**:
   - Each pass of the algorithm moves the largest unsorted element to its correct position at the end of the array.
   - The number of passes required is `n - 1`, where `n` is the number of elements in the array.

### Example
Consider an array `arr[] = {6, 0, 3, 5}`.

#### Passes:
1. **First Pass**: Place the largest element at the correct position.
2. **Second Pass**: Place the second-largest element at the correct position.
3. **Third Pass**: Place the remaining elements at their correct positions.

### Complexity Analysis
- **Time Complexity**: O(N^2)
- **Space Complexity**: O(1)

### Advantages
- Easy to understand and implement.
- Does not require additional memory space.
- Stable sorting algorithm.

### Disadvantages
- Time complexity of O(N^2), making it slow for large datasets.
- Requires a comparison operator, limiting efficiency in certain cases.

### FAQs 1. **What is the Boundary Case for Bubble Sort?** - Bubble sort takes minimum time (O(n)) when elements are
already sorted. It's best to check if the array is already sorted to avoid O(N^2) time complexity.

2. **Does sorting happen in place in Bubble sort?** - Yes, Bubble sort performs swapping of adjacent pairs without
additional data structures, making it an in-place algorithm.

3. **Is the Bubble sort algorithm stable?**
   - Yes, it is stable.

4. **Where is the Bubble sort algorithm used?** - It's often used in introductory lessons on sorting algorithms due
to its simplicity. It's also used in certain applications such as polygon filling algorithms in computer graphics."""


def Bubble_sort(arr, n):
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped in the inner loop, the array is sorted
        if not swapped:
            break
    return arr


li = [int(x) for x in input("Enter elements (separated by spaces): ").split()]
result = Bubble_sort(li, len(li))
print(result)
