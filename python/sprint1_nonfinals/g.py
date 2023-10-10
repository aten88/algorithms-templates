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


def read_input() -> int:
    return int(input().strip())


print(to_binary(read_input()))
