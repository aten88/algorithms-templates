def change_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        if min_index != i:
            temp = arr[min_index]
            arr[min_index] = arr[i]
            arr[i] = temp
    return arr


arr1 = [5, 3, 8, 4, 1]

print(change_sort(arr1))
