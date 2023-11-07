def merge_sorted(arr1, arr2):
    result = []
    while arr1 and arr2:
        if arr1[0] < arr2[0]:
            result.append(arr1.pop(0))
        else:
            result.append(arr2.pop(0))
    if arr1:
        result.extend(arr1)
    if arr2:
        result.extend(arr2)
    return result


def half_array(arr):
    if len(arr) == 1:
        return arr
    middle = len(arr) // 2
    left = half_array(arr[:middle])
    right = half_array(arr[middle:])
    return merge_sorted(left, right)


arr3 = [15, 7, 3, 15, 11, 9, 5, 18]
print(half_array(arr3))
