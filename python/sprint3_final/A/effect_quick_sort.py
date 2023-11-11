import random

alla = [5, 10, 'alla']
gena = [5, 10, 'gena']


def comparsion_elements(arr1, arr2):
    result = []
    if arr1[0] > arr2[0]:
        result.append(arr1[2])
    if arr1[0] == arr2[0]:
        if arr1[1] < arr2[1]:
            result.append(arr1[2])
        if arr1[1] == arr2[1]:
            if arr1[2] < arr2[2]:
                result.append(arr1[2])
            else:
                result.append(arr2[2])
        else:
            result.append(arr2[2])
    else:
        result.append(arr2[2])

    if len(result) > 0:
        return result[0]


def quick_sort(array):
    if len(array) > 1:
        x = int(array[random.randint(0, len(array)-1)][1])
        highest = [u for u in array if int(u[1]) > x]
        equivalent = [u for u in array if int(u[1]) == x]
        low = [u for u in array if int(u[1]) < x]
        array = quick_sort(highest) + equivalent + quick_sort(low)
    return array


def read_input():
    n = int(input())
    members_list = []
    for _ in range(n):
        member = input().strip().split()
        members_list.append(list(member))
    return n, members_list


def test():
    n, member_list = read_input()
    print(quick_sort(member_list))


if __name__ == '__main__':
    test()
