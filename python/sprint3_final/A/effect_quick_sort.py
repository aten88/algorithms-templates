def custom_sort_key(item):
    return (-int(item[1]), int(item[2]), item[0])


def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot_key = custom_sort_key(array[0])
    equal = [x for x in array if custom_sort_key(x) == pivot_key]
    less = [x for x in array if custom_sort_key(x) < pivot_key]
    greater = [x for x in array if custom_sort_key(x) > pivot_key]
    return quick_sort(greater) + equal + quick_sort(less)


def read_input():
    n = int(input())
    members_list = [None] * n
    for i in range(n):
        member = input().strip().split()
        members_list[i] = member
    return n, members_list


def test():
    n, member_list = read_input()
    for member in reversed(quick_sort(member_list)):
        print(member[0])


if __name__ == '__main__':
    test()
