def broken_search(nums, target) -> int:
    left = 0
    right = (len(nums) - 1)  # =8
    while left <= right:
        mid = (left + right) // 2  # =4
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


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    print(broken_search(arr, 100))
    # assert broken_search(arr, 5) == 6


if __name__ == '__main__':
    test()
