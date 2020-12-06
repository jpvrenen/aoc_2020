from modules.helpers import read_file
from collections import Counter


# path = 'C:\\DATA\\Projects\\aoc_2020'
# day = 'day6'
declarations = """abc

a
b
c

ab
ac

a
a
a
a

b"""

# declarations_string = re.split(r'(?:\r?\n){2,}', declarations)
# declarations_string = re.split(r'\n{2}', declarations)


def part_one(path, day):
    # declarations_string = declarations.split('\n\n')
    # collect answers where each element in list contains all answers from the group, individual member answers are
    # separated by '\n'
    declarations_file = read_file(f"{path}\\{day}\\declarationforms", empty_lines=True)
    # smash all individual answers into unique (set) given answer and count the char occurence
    count_occurrences = [len(set([y for y in x.replace('\n', '')])) for x in declarations_file]
    # sum all list items and print
    print(f"Solution {day} part 1: Sum of counts = {sum(count_occurrences)}")


def part_two(path, day):
    # declarations_string = declarations.split('\n\n')
    # collect answers where each element in list contains all answers from the group, individual member answers are
    # separated by '\n'
    declarations_file = read_file(f"{path}\\{day}\\declarationforms", empty_lines=True)
    # collect all answers but do not smash, also collect number of persons in group, put tuples in list
    all_answers = [(list([y for y in x.replace('\n', '')]), len(x.split('\n'))) for x in declarations_file]
    # count the same answers
    count_same_answer = list()
    for groupanswers in all_answers:  # groupanswers ([<all groupanswers>], <size of group>)
        answer_occurence = Counter(groupanswers[0])  # for all groupanswers count the occurence of each element
        nr_persons = groupanswers[1]  # number of people in group
        group_result = list()  # collect same answer given by group
        for key in answer_occurence:
            if answer_occurence[key] == nr_persons:  # if the occurence of anser matches the number of people in group
                group_result.append(key)
        if group_result:  # if the group has given same answer
            count_same_answer.append(len(group_result))
    print(f"Solution {day} part 2: Sum of count same answer = {sum(count_same_answer)}")
