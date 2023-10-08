from typing import List, Tuple


def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    result = []
    if row - 1 >= 0:
        neighbour_1 = matrix[row - 1][col]
        result.append(neighbour_1)
    if col + 1 < len(row):
        neighbour_2 = matrix[row][col + 1]
        result.append(neighbour_2)
    if row + 1 < len(matrix):
        neighbour_3 = matrix[row + 1][col]
        result.append(neighbour_3)
    if col - 1 >= 0:
        neighbour_4 = matrix[row][col - 1]
        result.append(neighbour_4)
    return result


def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col


matrix, row, col = read_input()
print(" ".join(map(str, get_neighbours(matrix, row, col))))
