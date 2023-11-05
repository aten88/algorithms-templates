def bracket_generator(n, open_count, close_count, s):
    if open_count + close_count == 2 * n:
        print(s)
        return
    if open_count < n:
        bracket_generator(n, open_count + 1, close_count, s + '(')
    if close_count < open_count:
        bracket_generator(n, open_count, close_count + 1, s + ')')


def read_input() -> int:
    n = int(input())
    return n


def main():
    n = read_input()
    bracket_generator(n, 0, 0, "")


if __name__ == '__main__':
    main()
