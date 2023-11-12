# Номер посылки 96956536

def custom_sort_key(item):
    ''' Задает порядок сравнения элементов. '''
    return (-int(item[1]), int(item[2]), item[0])


def quick_sort(array):
    ''' Метод быстрой сортировки. '''
    if len(array) <= 1:
        return array
    pivot_key = custom_sort_key(array[0])
    equal, less, greater = [], [], []
    for x in array:
        key = custom_sort_key(x)
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
