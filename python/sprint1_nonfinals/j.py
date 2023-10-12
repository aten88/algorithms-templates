from typing import List


def factorize(number: int) -> List[int]:
    factors = []
    while number % 2 == 0:
        factors.append(2)
        number = number // 2
    for i in range(3, int(number**0.5) + 1, 2):
        while number % i == 0:
            factors.append(i)
            number = number // i
    if number > 1:
        factors.append(number)

    return factors


result = factorize(int(input()))
print(" ".join(map(str, result)))
