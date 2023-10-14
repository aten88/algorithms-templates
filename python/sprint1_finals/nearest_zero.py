from typing import List

# id-посылки 92916328


def nearest_zero(arr: List[int]) -> List[int]:
    ''' Ищет расстояние до ближайшего 0. '''
    result = [0] * len(arr)
    left_zero = -1
    for i in range(len(arr)):
        if arr[i] == 0:
            left_zero = i
        if left_zero != -1:
            result[i] = i - left_zero

    right_zero = -1
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == 0:
            right_zero = i
        if right_zero != -1:
            result[i] = (
                min(result[i], right_zero - i)
                if result[i] != 0 else right_zero - i
            )

    return result


def read_input() -> List[int]:
    n = int(input())
    plots = list(map(int, input().strip().split()))
    return plots


plots = read_input()
print(' '.join(map(str, nearest_zero(plots))))
