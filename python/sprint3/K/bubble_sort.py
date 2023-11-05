def bubble_sort(n, arr):
    states = []

    def issorted(arr):
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

    if issorted(arr):
        states.append(arr.copy())
    else:
        for i in range(n):
            is_sorted = True
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    is_sorted = False
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            if not is_sorted:
                states.append(arr.copy())
            else:
                break

    for state in states:
        print(' '.join(map(str, state)))


def read_input() -> int:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    return n, arr


def main():
    n, arr = read_input()
    bubble_sort(n, arr)


if __name__ == '__main__':
    main()
