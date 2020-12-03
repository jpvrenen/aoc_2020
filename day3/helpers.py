from modules.helpers import read_file


trajectory = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""


def load_trajectory(data):
    """
    load trajectory data from input creates a list of lists each trajectory becomes list
    :param data: ['trajectory string', 'etc', .. ]
    :return: [[list of elements from trajectory data], [etc], [etc]]
    """
    result = list()
    for entry in data:
        result.append([x for x in entry])
    return result


def calc_offset(cur, add_nr, size):
    """
    calculate offset based on current offset and size of elements, offset cannot surpass size
    :param cur: current offset
    :param size: number of patterns
    :param add_nr: add number to offset
    :return: offset
    """
    new_offset = int(cur) + int(add_nr)
    if new_offset >= int(size):
        new_offset = new_offset - size
    return new_offset


def count_trees(traj_data, right, down):
    """
    based on the traj_data use right and down to count number of trees
    :param traj_data: [[list of elements from trajectory data], [etc], [etc]] with '.' = square and '#' = tree
    :param right: amount steps right
    :param down: amount steps down
    :return: number of trees encountered
    """
    trees = int()
    offset = 0
    traj_data = traj_data[::down]
    for entry in traj_data[1::]:
        offset = calc_offset(offset, right, len(entry))
        if entry[offset] == '#':
            trees += 1
    return trees


def part_one(path, day):
    # data_string = trajectory.split('\n')
    data_file = read_file(f"{path}\\{day}\\trajectory", as_lines=True)
    traj = load_trajectory(data_file)
    nr_trees = count_trees(traj, 3, 1)
    print(f"Solution {day} part 1: {nr_trees} trees")


def part_two(path, day):
    data_string = trajectory.split('\n')
    data_file = read_file(f"{path}\\{day}\\trajectory", as_lines=True)
    traj = load_trajectory(data_file)
    check_slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    multiply_trees = 1
    for slope in check_slopes:
        nr_trees = count_trees(traj, slope[0], slope[1])
        multiply_trees *= nr_trees
    print(f"Solution {day} part 2: {multiply_trees} multiplication of trees")
