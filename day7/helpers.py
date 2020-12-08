from modules.helpers import read_file
import re


# path = 'C:\\DATA\\Projects\\aoc_2020'
# day = 'day7'

bagrules = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
dark chartreuse bags contain 2 plaid black bags, 4 light bronze bags, 5 dotted cyan bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""


second_bagrules = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""


def split_stringlist(data, s):
    """
    From a list of strings chop on given parameter n
    :param data: list of strings ['', '', etc]
    :param s: char or word to
    :return: list of lists where each list is split on s
    """
    return [x.split(s) for x in data]


def extract_nr_bg(data):
    """
    for list find number and bag color
    :param data: ['s contain 1 bright white ', ', 2 muted yellow ', 's.']
    :return: [('bright white', 1), ('muted yellow', 2)]
    """
    re_nr_bc = re.compile(r'^.*(\d+)\s(\w+\s\w+)\s$')
    result = list()
    for x in data:
        match = re_nr_bc.match(x)
        if match:
            result.append((match.group(2), int(match.group(1))))
    return result


def sanitize_baglist(rawbaglist):
    """
    From given list of lists extract color and number
    :param rawbaglist: list elements containing bag color and amount
    :return: list of lists where [['bag color', ('bag color', nr), etc]]
    """
    result = list()
    for entry in rawbaglist:
        result_entry = [entry[0].strip()]
        result_entry.extend(extract_nr_bg(entry[1:]))
        result.append(result_entry)
    return result


def bagrules_dict(data):
    """
    from sanitized data create a dictionary with bagrules
    :param data: ['light red', ('bright white', 1), ('muted yellow', 2)]
    :return:
    """
    return {x[0]: dict(x[1:]) for x in data}


def find_more_bags(guide, bags):
    if bags:
        # print(f"{len(bags)} bags: {bags}")
        bag_result = list()
        for color in bags:
            for key in guide:
                if color in guide[key] and guide[key][color] >= 1:
                    # print(f"key: {key}, can contain at least {guide[key][color]} {color} bags.")
                    bag_result.append(key)
        bags.extend(find_more_bags(guide, list(set(bag_result))))
    return list(set(bags))


def count_bags(guide, bags):
    """
    recursion find all bags in bags until no more bag in bag, then recurse back and add all bags found
    :param guide: dictionary containing what color holds what bag and how much
    :param bags: dictionary with bags for which we need to find how many bags are in these bags
    :return: returns current bag count until all bags are counted
    """
    # print(f"=====")
    # print(f"find bags in: {bags.keys()}")
    bag_count = int()
    for color in bags:
        # print(f"{color}: has bags, {guide[color]}")
        if guide[color]:  # if bag still contain bag(s)
            # print(f"bag_count += {bags[color]} + {bags[color]} * {guide[color]}")
            has_bags = count_bags(guide, guide[color])
            bag_count += bags[color] + (bags[color] * has_bags)
            # print(f"{guide[color]} has {has_bags} bags.")
            # print(f"bag_count += {bags[color]} + {bags[color]} * {has_bags}")
            # print(f"if: bag_count is now: {bag_count}")
        else:  # no more bags are found, we recurse back
            bag_count += bags[color]
            # print(f"end of line, bag_count = {bags[color]}")
            # print(f"=====")
    return bag_count


def part_one(path, day):
    # bagrules_string = bagrules.split('\n')
    bagrules_file = read_file(f"{path}\\{day}\\bagrules", as_lines=True)
    baglist = split_stringlist(bagrules_file, 'bag')
    baglist_sanitized = sanitize_baglist(baglist)
    bagrules_guide = bagrules_dict(baglist_sanitized)
    get_bags = find_more_bags(bagrules_guide, ['shiny gold'])
    print(f"Solution {day} part 1: {len(get_bags) - 1} bag colors containing at least 1 shiny gold bag.")


def part_two(path, day):
    # s_bagrules_string = second_bagrules.split('\n')
    bagrules_file = read_file(f"{path}\\{day}\\bagrules", as_lines=True)
    baglist = split_stringlist(bagrules_file, 'bag')
    baglist_sanitized = sanitize_baglist(baglist)
    bagrules_guide = bagrules_dict(baglist_sanitized)
    get_bags = count_bags(bagrules_guide, {'shiny gold': 1})
    print(f"Solution {day} part 2: {get_bags - 1} individual bags required for 1 shiny gold bag.")
