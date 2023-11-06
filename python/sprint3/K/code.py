# def merge(arr, lf, mid, rg):
# 	# Your code
# 	# “ヽ(´▽｀)ノ”
# 	pass


# def merge_sort(arr, lf, rg):
# 	# Your code
# 	# “ヽ(´▽｀)ノ”
# 	pass


# def test():
# 	a = [1, 4, 9, 2, 10, 11]
# 	b = merge(a, 0, 3, 6)
# 	expected = [1, 2, 4, 9, 10, 11]
# 	assert b == expected
# 	c = [1, 4, 2, 10, 1, 2]
# 	merge_sort(c, 0, 6)
# 	expected = [1, 1, 2, 2, 4, 10]
# 	assert c == expected


# if __name__ == '__main__':
# 	test()

# arr1 = [7, 3, 11]
# arr2 = [13, 5, 9]

# arr1 = sorted(arr1)
# arr2 = sorted(arr2)


def array_sorted(arr1, arr2):
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


# print(mass_sorted(arr1, arr2))


def half_array(arr):
    if len(arr) == 1:
        return arr
    middle = len(arr) // 2
    left = half_array(arr[:middle])
    right = half_array(arr[middle:])
    return array_sorted(left, right)


arr3 = [15, 7, 3, 15, 11, 9, 5, 18]
print(half_array(arr3))
