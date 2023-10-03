from typing import List, Tuple


def moving_average(arr: List[int], window_size: int) -> List[float]:
    result = []
    current_sum = sum(arr[0:window_size])
    result.append(current_sum/window_size)
    for begin_index in range(0, len(arr) - window_size):
        current_sum -= arr[begin_index]
        current_sum += arr[begin_index + window_size]
        current_avg = current_sum / window_size
        result.append(current_avg)
    return result


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    window_size = int(input())
    return arr, window_size


arr, window_size = read_input()
print(" ".join(map(str, moving_average(arr, window_size))))
