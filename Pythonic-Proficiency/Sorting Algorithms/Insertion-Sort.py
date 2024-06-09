"""
## Insertion Sort Algorithm
Insertion sort is a simple and efficient sorting algorithm that works by iteratively inserting each element of an unsorted list into its correct position in a sorted portion of the list. It's a stable sorting algorithm, meaning elements with equal values maintain their relative order in the sorted output.

### How it Works
1. **Initialization**:
   - Start with the second element of the array as the first element is assumed to be sorted.

2. **Insertion Process**:
   - Compare each element with the elements before it in the sorted portion.
   - Swap elements as necessary to place the current element in its correct position among the sorted elements.

3. **Repeat**:
   - Continue this process for each element until the entire array is sorted.

### Example
Consider an array `arr[] = {23, 1, 10, 5, 2}`.

#### Passes:
1. **First Pass**: Place each element in its correct position among the first two elements.
2. **Second Pass**: Place each element in its correct position among the first three elements.
3. **Third Pass**: Place each element in its correct position among the first four elements.
4. **Fourth Pass**: Place each element in its correct position among the first five elements.

### Complexity Analysis
- **Time Complexity**:
   - Best case: O(n) (if already sorted)
   - Average case: O(n^2)
   - Worst case: O(n^2)
- **Space Complexity**: O(1)

### Advantages
- Simple and easy to implement.
- Stable sorting algorithm.
- Efficient for small and nearly sorted lists.
- Space-efficient.

### Disadvantages
- Inefficient for large lists.
- Not as efficient as other algorithms for most cases.

### Applications
Insertion sort is commonly used when:
- The list is small or nearly sorted.
- Simplicity and stability are important.

### FAQs
1. **Boundary Cases of Insertion Sort**:
   - Insertion sort takes the maximum time if elements are sorted in reverse order and minimum time if elements are already sorted.
2. **Algorithmic Paradigm**:
   - Insertion sort follows an incremental approach.
3. **In-place Sorting**:
   - Yes, insertion sort is an in-place sorting algorithm.
4. **Stability**:
   - Yes, insertion sort is stable.
5. **Usage**:
   - Insertion sort is used for small lists or when simplicity and stability are crucial.
"""


def Insertion_Sort(arr, n):
    for i in range(1, n):
        j = i - 1
        temp = arr[i]
        while j >= 0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
    return arr


li = [int(x) for x in input("Enter elements (separated by spaces): ").split()]
result = Insertion_Sort(li, len(li))
print(result)
