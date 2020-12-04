import re
from modules.helpers import read_passwords_file


passports = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

invalid_passports = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""

valid_passports = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""


def listdicts_from_liststrings(liststrings):
    """
    function that returns list of dicts from list of strings where string contains key value pairs separated by space or
    newline
    :param liststrings: ['key:value key:value\nkey:value etc', '', etc]
    :return: list of dicts
    """
    l_of_l = [re.split('\s|\\n', x) for x in liststrings]  # create list of lists split on space or newline
    result = [{y.split(':')[0]: y.split(':')[1] for y in x} for x in l_of_l]  # dict comp in list comp
    return result


def count_valid_passports(data, **kwargs):
    """
    count valid passports
    :param data: passport db
    :return: number of valid passports
    """
    mode = kwargs.get('mode', 'basic')
    count = 0
    if mode == 'basic':
        count = [valid_passport_basic(passp) for passp in data].count(True)
    elif mode == 'advanced':
        count = [valid_passport_advanced(passp) for passp in data].count(True)
    return count


def valid_passport_basic(passport):
    """
    Check if given passport is valid, returns True or False.
    Passports are valid if they contain elements:
    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)  # missing cid counts as valid
    :param passport: passport to validate
    :return: True when valid or False when invalid
    """
    valid_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
    passport_keys = set(passport.keys())
    diff_keys = list(valid_keys - passport_keys)
    nr_diff_keys = len(diff_keys)
    # if all keys are present, it is valid
    if nr_diff_keys == 0:
        return True
    # if passport is missing 1 item and it is cid, it is still valid
    elif nr_diff_keys == 1 and 'cid' in diff_keys:
        return True
    # if passport is missing 2 or more items, it is invalid
    elif nr_diff_keys >= 2:
        return False


def valid_byr(byr):
    """
    validate byr
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    :param byr: Birth Year
    :return: True if valid or False if invalid
    """
    try:
        if 1920 <= int(byr) <= 2002:
            return True
        return False
    except ValueError:
        return False


def valid_iyr(iyr):
    """
    validate iyr
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    :param iyr: Issue Year
    :return: True if valid or False if invalid
    """
    try:
        if 2010 <= int(iyr) <= 2020:
            return True
        return False
    except ValueError:
        return False


def valid_eyr(eyr):
    """
    validate eyr
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    :param eyr: Birth Year
    :return: True if valid or False if invalid
    """
    try:
        if 2020 <= int(eyr) <= 2030:
            return True
        return False
    except ValueError:
        return False


def valid_hgt(hgt):
    """
    validate hgt
    hgt (Height) - a number followed by either cm or in:
      If cm, the number must be at least 150 and at most 193.
      If in, the number must be at least 59 and at most 76.
    :param hgt: Height
    :return: True if valid or False if invalid
    """
    try:
        match_hgt_unit = re.compile(r'^(\d+)(cm|in)$')
        height = int(match_hgt_unit.match(hgt).group(1))
        unit = match_hgt_unit.match(hgt).group(2)
        # cm
        if unit == 'cm' and (150 <= height <= 193):
            return True
        # in
        if unit == 'in' and (59 <= height <= 76):
            return True
        return False
    except AttributeError:
        return False


def valid_hcl(hcl):
    """
    validate hcl
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    :param hcl: Hair Color
    :return: True if valid or False if invalid
    """
    match_hcl = re.compile(r'^#[0-9a-z]{6}$')
    if match_hcl.match(hcl):
        return True
    return False


def valid_ecl(ecl):
    """
    validate ecl
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    :param ecl: Eye Color
    :return: True if valid or False if invalid
    """
    eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if ecl in eye_colors:
        return True
    return False


def valid_pid(pid):
    """
    validate pid
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    :param pid: Passport ID
    :return: True if valid or False if invalid
    """
    match_pid = re.compile(r'^\d{9}$')
    passport_id = match_pid.match(pid)
    if passport_id:
        return True
    return False


def passport_val_checks(passport):
    """
    perform all validation checks needed to validate passport. 'cid' is valid by default since there is no check
    for cid.
    :param passport: perform validation checks
    :return: True if all checks pass, False if any check fails
    """
    if not valid_byr(passport['byr']):
        # print(f"Birth Year: {valid_byr(passport['byr'])}")
        return False
    if not valid_iyr(passport['iyr']):
        # print(f"Issue Year: {valid_iyr(passport['iyr'])}")
        return False
    if not valid_eyr(passport['eyr']):
        # print(f"Expiration Year: {valid_eyr(passport['eyr'])}")
        return False
    if not valid_hgt(passport['hgt']):
        # print(f"Height: {valid_hgt(passport['hgt'])}")
        return False
    if not valid_hcl(passport['hcl']):
        # print(f"Hair Color): {valid_hcl(passport['hcl'])}")
        return False
    if not valid_ecl(passport['ecl']):
        # print(f"Eye Color: {valid_ecl(passport['ecl'])}")
        return False
    if not valid_pid(passport['pid']):
        # print(f"Passport ID: {valid_pid(passport['pid'])}")
        return False
    return True


def valid_passport_advanced(passport):
    """
    Check if given passport is valid, returns True or False.
    Passports are valid when:
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    :param passport: passport to validate
    :return: True when valid or False when invalid
    """
    valid_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
    passport_keys = set(passport.keys())
    diff_keys = list(valid_keys - passport_keys)
    nr_diff_keys = len(diff_keys)
    # if all keys are present, we check values if they are valid
    if nr_diff_keys == 0:
        return passport_val_checks(passport)
    # if passport is missing 1 item and it is cid, we check values if they are valid except cid
    elif nr_diff_keys == 1 and 'cid' in diff_keys:
        return passport_val_checks(passport)
    # if passport is missing 2 or more items, it is invalid
    elif nr_diff_keys >= 2:
        return False


def part_one(path, day):
    # passport_string = passports.split('\n\n')
    # invalid_passp_string = invalid_passports.split('\n\n')
    # valid_passp_string = valid_passports.split('\n\n')
    passport_file = read_passwords_file(f"{path}\\{day}\\passports")
    passport_db = listdicts_from_liststrings(passport_file)
    valid_passports_b = count_valid_passports(passport_db)
    print(f"Solution {day} part 1: {valid_passports_b} valid passports counted")


def part_two(path, day):
    # passport_string = passports.split('\n\n')
    # invalid_passp_string = invalid_passports.split('\n\n')
    # valid_passp_string = valid_passports.split('\n\n')
    passport_file = read_passwords_file(f"{path}\\{day}\\passports")
    passport_db = listdicts_from_liststrings(passport_file)
    valid_passports_a = count_valid_passports(passport_db, mode='advanced')
    print(f"Solution {day} part 2: {valid_passports_a} valid passports counted")
