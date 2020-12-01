from functools import reduce


def subtract_and_find(number, data):
    """
    We find 'number' as a sum for given datapoints
    :param number: number we need to find
    :param data: list of numbers any 2 members sum to 'number'
    :return: numbers that sum 'number'
    """
    for first_nr in data:
        second_nr = int(number) - int(first_nr)
        if second_nr in data:
            return [first_nr, second_nr]
    return []


def multiply_nrs(data):
    """
    Multiply numbers from list
    :param data: list with numbers
    :return: numbers from list multiplied
    """
    return reduce((lambda x, y: int(x) * int(y)), data)
