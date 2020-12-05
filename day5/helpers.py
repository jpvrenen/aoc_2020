from modules.helpers import read_file
import re

proj_path = 'C:\\DATA\\Projects\\aoc_2020'
today = 'day5'
boarding_passes = """BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL"""


def bin_conversion(data):
    """
    Converts data list of given characters into binary list
    :param data: input list ['FFFFFFFLLL', 'BBBBBBBRRR', etc]
    :return: output list ['1111111111', '0000000000', etc]
    """
    result = list()
    for strentry in data:
        binentry = re.sub(r'[F|L]', '1', strentry)
        binentry = re.sub(r'[B|R]', '0', binentry)
        result.append(binentry)
    return result


def bin_flip(data):
    """
    Flip string binary values from 1 into bin 0 and 0 into bin 1, split binaries in 2 parts as tuples
    :param data: list of binaries ['1111111111', '0000000000', etc]
    :return: list of flipped binaries [(0b0000000, 0b000), (0b1111111, 0b111), etc]
    """
    result = [(bin(int(x[:7], 2) ^ 0b1111111), bin(int(x[7:10], 2) ^ 0b111)) for x in data]
    return result


def get_row_column(binaries):
    """
    From list of tuple(row, column) binaries retrieve row and column as int return as list of tuples
    :param binaries: [(0b0000000, 0b000), (0b1111111, 0b111), etc]
    :return: [(0, 0), (127, 8), etc]
    """
    result = [(int(x[0], 2), int(x[1], 2)) for x in binaries]
    return result


def get_seat_id(rowcolumns):
    """
    Calculate seat ids from given rowcolumns, row * 8 + column
    :param rowcolumns: [(0, 0), (127, 8), etc] where (row, column)
    :return: list with seat id's
    """
    result = [x[0] * 8 + x[1] for x in rowcolumns]
    return result


def part_one(path, day):
    # boarding_passes_string = boarding_passes.split('\n')
    # bin_boarding_passes_s = bin_conversion(boarding_passes_string)
    boarding_passes_file = read_file(f"{path}\\{day}\\boardingpasses", as_lines=True)
    bin_boarding_passes = bin_conversion(boarding_passes_file)
    bin_flipped = bin_flip(bin_boarding_passes)
    row_column_db = get_row_column(bin_flipped)
    seat_id_db = get_seat_id(row_column_db)
    print(f"Solution {day} part 1: Highest seat id = {max(seat_id_db)}")


def part_two(path, day):
    boarding_passes_file = read_file(f"{path}\\{day}\\boardingpasses", as_lines=True)
    bin_boarding_passes = bin_conversion(boarding_passes_file)
    bin_flipped = bin_flip(bin_boarding_passes)
    row_column_db = get_row_column(bin_flipped)
    seat_id_db = get_seat_id(row_column_db)
    all_seat_ids = set([x for x in range(min(seat_id_db), max(seat_id_db) + 1)])
    my_seat_id = all_seat_ids - set(seat_id_db)
    print(f"Solution {day} part 2: My seat id = {my_seat_id}")
