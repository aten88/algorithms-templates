# Номер посылки 96810272

def broken_search(nums, target) -> int:
    ''' Метод нахождения элемента в смещенном массиве. '''
    left = 0
    right = (len(nums) - 1)
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target and target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def read_input():
    ''' Метод чтения данных. '''
    len_array = int(input())
    target = int(input())
    array = list(map(int, input().split(' ')))
    return len_array, target, array


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    broken_search(arr, 100)
    assert broken_search(arr, 5) == 6
    len_arr, target, array = read_input()
    return broken_search(array, target)


if __name__ == '__main__':
    print(test())
