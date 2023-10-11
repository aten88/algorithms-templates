from typing import Tuple


def get_sum(first_number: str, second_number: str) -> str:

    def get_number(string: str):
        weight_byte = []
        for degree in range(len(string)):
            weight_byte.append(2**degree)
        weight_byte = weight_byte[::-1]

        result = []
        for i in range(len(string)):
            result.append(int(string[i]) * weight_byte[i])
        return sum(result)

    def to_binary(number: int) -> str:
        if number == 0:
            return 0
        result = []
        divisor = 2
        while number >= divisor-1:
            result.append(number % divisor)
            number = number // divisor
        result = result[::-1]
        answer = map(str, result)
        answer = ''.join(answer)
        return int(answer)

    return to_binary(get_number(first_number) + get_number(second_number))


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


first_number, second_number = read_input()
print(get_sum(first_number, second_number))
