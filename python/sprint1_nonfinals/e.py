def get_longest_word(line: str) -> str:
    words = line.split(' ')
    longest_word = []
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


def read_input() -> str:
    _ = input()
    line = input().strip()
    return line


def print_result(result: str) -> None:
    print(result)
    print(len(result))


print_result(get_longest_word(read_input()))
