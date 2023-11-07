from typing import List, Tuple


def read_input() -> Tuple[int, List[Tuple[str, int]]]:
    count = int(input())
    flowerbeds = []
    for i in range(count):
        flowerbed = list(map(int, input().split(' ')))
        flowerbeds.append(flowerbed)
    return count, flowerbeds


def cloumb(count, flowerbeds):
    result = []
    flowerbeds = sorted(flowerbeds, key=lambda i: [i[0], i[1]])
    for i in range(count-1):
        if (flowerbeds[i][1] >= flowerbeds[i+1][0]):
            flowerbeds[i+1][0] = min(flowerbeds[i][0], flowerbeds[i+1][0])
            flowerbeds[i+1][1] = max(flowerbeds[i][1], flowerbeds[i+1][1])
        else:
            result.append(flowerbeds[i])
    result.append(flowerbeds[-1])
    for i in result:
        print(*i)


def main():
    count, flowerbeds = read_input()
    cloumb(count, flowerbeds)


if __name__ == '__main__':
    main()
