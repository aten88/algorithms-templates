from typing import List

# id-посылки: 93183824


def count_points(k, buttons):
    ''' Считает количество очков. '''
    pushes_count = k * 2
    scores = 0
    buttons = [list(row.replace('.', '')) for row in buttons]
    count_dict = {str(i): 0 for i in range(1, 10)}
    for row in buttons:
        for char in row:
            if char in count_dict:
                count_dict[char] += 1

    for key, value in count_dict.items():
        if pushes_count >= value and value != 0:
            scores += 1
    return scores


def read_input() -> List[int]:
    k = int(input())
    buttons = [input() for _ in range(4)]
    return k, buttons


if __name__ == '__main__':
    k, buttons = read_input()
    print(count_points(k, buttons))
