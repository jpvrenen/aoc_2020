from modules.helpers import read_file
import re
import copy

# use list index to track for each line of code
# path = 'C:\\DATA\\Projects\\aoc_2020'
# day = 'day8'

bc = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


def get_instr(i):
    """
    From given parameter get individual elements
    :param i: instruction i.e. 'acc +1'
    :return: dictionary containing {c: {instr: <instruction>, op: '<operation>'}
    """
    # instr = re.compile(r'^(\w+)\s([+, -])(\d+)$')
    instr = re.compile(r'^(\w+)\s([+, -]\d+)$')
    m_instr = instr.match(i)
    instruction = m_instr.group(1)
    operation = m_instr.group(2)
    # nr = int(m_instr.group(3))
    result = {'c': {'instr': instruction, 'op': operation}}
    return result


def sanitize_bootcode(raw_code):
    """
    from given raw code return sanitized code
    :param raw_code: list of instructions where instruction is a string ['nop +0', 'acc +1', etc]
    :return: list of dictionaries, order is important [{c: {instr: <instruction>, op: '<operation>'}, etc]
    """
    return [get_instr(x) for x in raw_code]


def get_instr_index(code, instr):
    """
    retrieves instruction and it's index from the bootcode
    :param code: list of dictionaries [{c: {instr: <instruction>, op: '<operation>'}, etc]
    :param instr: instruction to look for
    :return: list of positions where the instruction is in the code
    """
    result = list()
    for n in range(len(code)):
        if code[n]['c']['instr'] == instr:
            result.append(n)
    return result


def run_bootcode(code, r):
    """
    runs bootcode with loopprevention exits when loop is detected and returns acc value on exit
    :param r: flag needed to print specific content
    :param code: bootcode to execute
    :return: acc value before going into loop
    """
    acc = 0
    runcode = True
    p_track = list()
    pointer = 0
    while runcode:
        p_track.append(pointer)
        # print(pointer)
        instr = code[pointer]
        if instr['c']['instr'] == 'acc':
            acc = eval(f"{acc} {instr['c']['op']}")
            pointer += 1
            # print(f"{instr['c']['instr']}: {instr['c']['op']}, acc = {acc}, pointer:{pointer}")
        elif instr['c']['instr'] == 'nop':
            pointer += 1
            # print(f"{instr['c']['instr']}: {instr['c']['op']}, acc = {acc}, pointer:{pointer}")
        elif instr['c']['instr'] == 'jmp':
            jmp_pointer = eval(f"{pointer} {instr['c']['op']}")
            if pointer == jmp_pointer:
                # print(f"Infinite loop prevention, pointer:{pointer}")
                runcode = False
            else:
                pointer = jmp_pointer
                # print(f"{instr['c']['instr']}: {instr['c']['op']}, acc = {acc}, pointer:{pointer}")
        else:
            pointer += 1
            # print(f"{instr['c']}: pointer:{pointer}")
        if not runcode:
            return False
        if pointer in p_track:
            # print("==========")
            if r == 1:
                print(f"Loop prevention, value of acc: {acc}, pointer:{pointer} already executed! ")
            # print("==========")
            runcode = False
        elif pointer == len(code):
            # print(f"Outside code boundary, pointer:{pointer}")
            print(f"Normal execution, value of acc: {acc}, pointer:{pointer}")
            return True
        elif pointer < 0:
            return False
        elif pointer > len(code):
            return False


def part_one(path, day):
    raw_bootcode_s = bc.split('\n')
    raw_bootcode_f = read_file(f"{path}\\{day}\\bootcode", as_lines=True)
    bootcode = sanitize_bootcode(raw_bootcode_f)
    run_bootcode(bootcode, 1)


def part_two(path, day):
    raw_bootcode_s = bc.split('\n')
    raw_bootcode_f = read_file(f"{path}\\{day}\\bootcode", as_lines=True)
    bootcode = sanitize_bootcode(raw_bootcode_f)
    swap_inst = [('jmp', 'nop'), ('nop', 'jmp')]
    for inst in swap_inst:
        si_index = get_instr_index(bootcode, inst[0])
        for si in si_index:
            copy_bootcode = copy.deepcopy(bootcode)
            copy_bootcode[si]['c']['instr'] = inst[1]
            result = run_bootcode(copy_bootcode, 2)
            if result:
                print("=====")
                print(f"swap: {inst[0]} for {inst[1]} at index: {si}")
                return
