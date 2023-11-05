PHONE_KEYS = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def generate_combinations(lists, current_string='', result=None):
    if result is None:
        result = []
    if not lists:
        result.append(current_string)
        return
    for char in lists[0]:
        generate_combinations(lists[1:], current_string + char, result)
    return result


def read_input() -> int:
    keys_list = input()
    return keys_list


def main():
    keys_list = read_input()
    variables = [i for i in keys_list]
    pushed_keys_list = []
    for char in variables:
        if char in PHONE_KEYS.keys():
            pushed_keys_list.append(PHONE_KEYS.get(char))
        else:
            print('Нет совпадений в словаре. ')
    print(' '.join(generate_combinations(pushed_keys_list)))


if __name__ == '__main__':
    main()
