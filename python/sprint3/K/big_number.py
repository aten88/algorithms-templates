from functools import cmp_to_key


def compare(x, y):
    xy = str(x) + str(y)
    yx = str(y) + str(x)
    return int(yx) - int(xy)


def max_number(nums):
    nums.sort(key=cmp_to_key(compare))
    return ''.join(map(str, nums))


def read_input() -> int:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    return n, arr


def main():
    n, arr = read_input()
    print(max_number(arr))


if __name__ == '__main__':
    main()
