def subtract_and_find(number, data):
    """
    We find 'number' as a sum for given datapoints
    :param number: number we need to find
    :param data: list of numbers any 2 members sum to 'number'
    :return: numbers that sum 'number'
    """
    for entry in data:
        find_nr = int(number) - int(entry)
        if find_nr in data:
            return [entry, find_nr]
    return []
