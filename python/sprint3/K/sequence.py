def read_input() -> str:
    s = str(input())
    t = str(input())
    return s, t


def is_subsequence(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)


def main():
    s, t = read_input()
    if is_subsequence(s, t):
        return True
    else:
        return False


if __name__ == '__main__':
    print(main())
