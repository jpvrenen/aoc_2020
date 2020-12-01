from functools import reduce
from itertools import combinations


def multiply_nrs(data):
    """
    Multiply numbers from list
    :param data: list with numbers
    :return: numbers from list multiplied
    """
    return reduce((lambda x, y: int(x) * int(y)), data)


def get_combinations(data, r):
    """
    returns list with combinations from data
    :param data: list to combine
    :param r: create nr combinations from input list
    :return: list with combinations
    """
    return list(combinations(data, r))


def sum_combinations(data, number):
    """
    returns numbers from combination list that sum given number
    :param data: list of combinations numbers
    :param number: number should be equal the sum of combinations in list
    :return: list of combinations that meet the criteria
    """
    result = list()
    for n in range(len(data)):
        if number == sum(data[n]):
            result.extend(list(data[n]))
    return result
