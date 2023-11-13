# Номер посылки 97114093

from typing import List


def custom_sort_key(item: List[int]) -> List[int]:
    ''' Задает порядок сравнения элементов. '''
    return (-int(item[1]), int(item[2]), item[0])


def quick_sort(array: List[int]) -> List[int]:
    ''' Метод быстрой сортировки. '''
    if len(array) <= 1:
        return array
    pivot_key = array[0]
    equal, less, greater = [], [], []
    for x in array:
        key = x
        if key == pivot_key:
            equal.append(x)
        elif key < pivot_key:
            less.append(x)
        else:
            greater.append(x)
    return quick_sort(greater) + equal + quick_sort(less)


def read_input():
    ''' Метод чтения данных. '''
    n = int(input())
    members_list = [custom_sort_key(input().strip().split()) for _ in range(n)]
    return n, members_list


def test():
    n, member_list = read_input()
    for member in reversed(quick_sort(member_list)):
        print(member[2])


if __name__ == '__main__':
    test()
