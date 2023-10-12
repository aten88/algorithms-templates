from typing import List


def nearest_zero(arr: List[int]) -> List[int]:
    result = []
    for i in range(len(arr)):
        if arr[i] == 0:
            result.append(0)
        else:
            steps_right = float('inf')
            steps_left = float('inf')
            for r in range(i + 1, len(arr)):
                if arr[r] == 0:
                    steps_right = r - i
                    break
            for left in range(i - 1, -1, -1):
                if arr[left] == 0:
                    steps_left = i - left
                    break
            min_dist = min(steps_right, steps_left)
            result.append(min_dist)

    return result


def read_input() -> List[int]:
    n = int(input())
    plots = list(map(int, input().strip().split()))
    return plots


plots = read_input()
print(' '.join(map(str, nearest_zero(plots))))
