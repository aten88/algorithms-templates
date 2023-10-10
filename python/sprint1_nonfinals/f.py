def is_palindrome(line: str) -> bool:
    line = line.lower()
    line = ''.join(filter(str.isalnum, line))
    return line == line[::-1]


print(is_palindrome(input().strip()))
