from modules.helpers import read_file
from itertools import combinations

# path = 'C:\\DATA\\Projects\\aoc_2020'
# day = 'day9'

enc = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


def check_preamble_sum(pre, n):
    """
    Check for given preamble combinations if any combination add up to given sum number
    :param pre: list of preamble combinations
    :param n: number any of the preamble combination needs to match
    :return: True if any preamble combinatoin match n False otherwise
    """
    for p in pre:
        if sum(p) == n:
            return True
    return False


def check_preamble_sum2(pre, n):
    """
    Check for given preamble combinations if any combination add up to given sum number
    :param pre: list of preamble combinations
    :param n: number any of the preamble combination needs to match
    :return: True if any preamble combinatoin match n False otherwise
    """
    for p in pre:
        if sum(p) == n:
            return p
    return []


def get_combinations(data):
    """
    Get possible contiguous list combinations from list data minimum of 2 until max of data list elements
    :param data: list of numbers
    :return: combinations from list ranging from 2 until len(data)
    """
    result = list()
    for y in range(2, len(data)+1):
        stop = y - 1
        begin = 0
        end = y
        for _ in range(len(data)-stop):
            result.append(data[begin:end])
            begin += 1
            end += 1
    return result


def part_one(path, day):
    # raw_encoding_s = enc.split('\n')
    raw_encoding_f = read_file(f"{path}\\{day}\\encoding", as_lines=True)
    # encoding_s = [int(x) for x in raw_encoding_s]
    encoding_f = [int(x) for x in raw_encoding_f]
    # preamble_list = encoding_s[:5]
    # rest_list = encoding_s[5:]
    preamble_list = encoding_f[:25]
    rest_list = encoding_f[25:]

    while rest_list:
        sum_entry = rest_list.pop(0)
        preamble_comb = list(combinations(preamble_list, 2))
        preamble_sum = check_preamble_sum(preamble_comb, sum_entry)
        if preamble_sum:
            preamble_list.pop(0)
            preamble_list.append(sum_entry)
        else:
            print(f"Number: {sum_entry} cannot be formed by any combination of {preamble_list}!")
            return sum_entry


def part_two(path, day):
    # raw_encoding_s = enc.split('\n')
    raw_encoding_f = read_file(f"{path}\\{day}\\encoding", as_lines=True)
    # encoding_s = [int(x) for x in raw_encoding_s]
    encoding_f = [int(x) for x in raw_encoding_f]
    # preamble_list = encoding_s[:5]
    # rest_list = encoding_s[5:]
    preamble_list = encoding_f[:25]
    rest_list = encoding_f[25:]
    # invalid_number = 88311122
    invalid_number = part_one(path, day)
    # preamble_comb = get_multiple_combinations(preamble_list)
    # preamble_sum = check_preamble_sum2(preamble_comb, invalid_number)
    found = False
    while not found and rest_list:
        preamble_comb = get_combinations(preamble_list)
        check_sum = check_preamble_sum2(preamble_comb, invalid_number)
        if check_sum:
            check_sum.sort()
            print(f"sum of 1st and last contiguous range: {check_sum[0] + check_sum[-1]}, "
                  f"preamble list:{check_sum}")
            found = True
        else:
            preamble_list.pop(0)
            preamble_list.append(rest_list.pop(0))
