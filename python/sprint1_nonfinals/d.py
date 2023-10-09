from typing import List


def get_weather_randomness(temperatures: List[int]) -> int:
    result = []
    n = len(temperatures)

    if n <= 1:
        return 1

    if temperatures[0] > temperatures[1]:
        result.append(temperatures[0])
    if temperatures[len(temperatures)-1] > temperatures[len(temperatures)-2]:
        result.append(temperatures[len(temperatures)-1])

    for index in range(1, n - 1):
        current_element = temperatures[index]
        previous_element = temperatures[index - 1]
        next_element = temperatures[index + 1]

        if (
            current_element > previous_element
            and current_element > next_element
        ):
            result.append(current_element)

    return len(result)


def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures


temperatures = read_input()
print(get_weather_randomness(temperatures))
