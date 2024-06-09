def merge(arr1, arr2, n, m):
    i = 0
    j = 0
    arr = []
    while i < n and j < m:
        if arr1[i] <= arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
    while i < n:
        arr.append(arr1[i])
        i += 1
    while j < m:
        arr.append(arr2[j])
        j += 1
    return arr


l1 = [1, 4, 9, 10]
l2 = [2, 3, 6, 7, 8]
result = merge(l1, l2, len(l1), len(l2))
print(result)
