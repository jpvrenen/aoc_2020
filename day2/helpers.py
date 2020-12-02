from modules.helpers import read_file


passwords = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""


def valid_occurence_posminmax(itemlist, item, posmin, posmax):
    """
    returns true if item meets requirement
    :param itemlist: list of items
    :param item: find item in list of items
    :param posmin: item should be at pos_min
    :param posmax: item should be at pos_max
    :return: True if item meets posmin posmax requirement
    """
    if itemlist[posmin - 1] == item and itemlist[posmax - 1] == item:
        return False
    if itemlist[posmin - 1] == item or itemlist[posmax - 1] == item:
        return True
    else:
        return False


def valid_occurence_minmax(itemlist, item, minimum, maximum):
    """
    returns true if item meets requirement
    :param itemlist: list of items
    :param item: find item in list of items
    :param minimum: minimum amount item should exist
    :param maximum: maximum amount item should exist
    :return: True if item meets min max requirement
    """
    count_item = itemlist.count(item)
    if minimum <= count_item <= maximum:
        return True
    else:
        return False


def minmax(mmdata):
    """
    return dict with values min and max
    :param mmdata: string using format '<min_oc>-<max_oc>'
    :return:
    """
    mm_min = int(mmdata.split('-')[0])
    mm_max = int(mmdata.split('-')[1])
    return {'min': mm_min, 'max': mm_max}


def get_parameters(entry):
    """
    Get parameters from entry using specific format
    :param entry: string using format '<min_oc>-<max_oc> <letter>: <passwd>'
    :return: dict with extracted parameters
    """
    parameters = dict()
    entry = entry.rstrip('\n')
    param = entry.split()
    mm = minmax(param[0])
    parameters['min_oc'] = mm['min']
    parameters['max_oc'] = mm['max']
    parameters['letter'] = param[1].rstrip(':')
    parameters['passwd'] = list(param[2])
    return parameters


def part_one(path, day):
    # data = passwords.split('\n')
    data = read_file(f"{path}\\{day}\\passwords", as_lines=True)
    valid_passwd = int()
    for entry in data:
        p = get_parameters(entry)
        valid = valid_occurence_minmax(p['passwd'], p['letter'], p['min_oc'], p['max_oc'])
        if valid:
            valid_passwd += 1
    print(f"Solution {day} part 1: {valid_passwd} valid password(s)")


def part_two(path, day):
    # data = passwords.split('\n')
    data = read_file(f"{path}\\{day}\\passwords", as_lines=True)
    valid_passwd = int()
    for entry in data:
        p = get_parameters(entry)
        valid = valid_occurence_posminmax(p['passwd'], p['letter'], p['min_oc'], p['max_oc'])
        if valid:
            valid_passwd += 1
    print(f"Solution {day} part 2: {valid_passwd} valid password(s)")
