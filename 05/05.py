def read_file(filename):
    with open(filename, "r") as f:
        line = f.readline()
        return [int(i) for i in line.split(",")]


def get_modes(modes):
    return [int(mode) for mode in [modes[2], modes[1], modes[0], modes[3:]]]


def get_value(mode, increment, idx, list_all):
    if mode == 0:  # position mode
        position = list_all[idx + increment]
        return list_all[position]
    immediate = idx + increment
    return list_all[immediate]  # immediate mode


def get_values(mode_1_pm, mode_2_pm, idx, list_all):
    return get_value(mode_1_pm, 1, idx, list_all), get_value(mode_2_pm, 2, idx, list_all)


def add(mode_1_pm, mode_2_pm, idx, list_all):
    value_1, value_2 = get_values(mode_1_pm, mode_2_pm, idx, list_all)
    list_all[list_all[idx + 3]] = value_1 + value_2


def multiply(mode_1_pm, mode_2_pm, idx, list_all):
    value_1, value_2 = get_values(mode_1_pm, mode_2_pm, idx, list_all)
    list_all[list_all[idx + 3]] = value_1 * value_2


def jump_if_true(mode_1_pm, mode_2_pm, idx, list_all):
    value_1, value_2 = get_values(mode_1_pm, mode_2_pm, idx, list_all)
    if value_1 != 0:
        return value_2
    return idx + 3


def jump_if_false(mode_1_pm, mode_2_pm, idx, list_all):
    value_1, value_2 = get_values(mode_1_pm, mode_2_pm, idx, list_all)
    if value_1 == 0:
        return value_2
    return idx + 3


def less_than(mode_1_pm, mode_2_pm, idx, list_all):
    value_1, value_2 = get_values(mode_1_pm, mode_2_pm, idx, list_all)
    if value_1 < value_2:
        list_all[list_all[idx + 3]] = 1
    else:
         list_all[list_all[idx + 3]] = 0


def equals(mode_1_pm, mode_2_pm, idx, list_all):
    value_1, value_2 = get_values(mode_1_pm, mode_2_pm, idx, list_all)
    if value_1 == value_2:
        list_all[list_all[idx + 3]] = 1
    else:
         list_all[list_all[idx + 3]] = 0


def user_input():
    user_input = input("Enter input: ")
    return int(user_input)


def run(list_all):
    idx = 0
    diagnostic_code = None

    while list_all[idx] != 99:
        mode1, mode2, mode3, opcode = get_modes(f"{list_all[idx]:05}")

        if opcode == 1:
            add(mode1, mode2, idx, list_all)
            idx += 4

        elif opcode == 2:
            multiply(mode1, mode2, idx, list_all)
            idx += 4

        elif opcode == 3:
            position_for_output = list_all[idx + 1]
            list_all[position_for_output] = user_input()
            idx += 2

        elif opcode == 4:
            position_for_output = list_all[idx + 1]
            diagnostic_code = list_all[position_for_output]
            idx += 2

        elif opcode == 5:
            idx = jump_if_true(mode1, mode2, idx, list_all)

        elif opcode == 6:
            idx = jump_if_false(mode1, mode2, idx, list_all)

        elif opcode == 7:
            less_than(mode1, mode2, idx, list_all)
            idx += 4

        elif opcode == 8:
            equals(mode1, mode2, idx, list_all)
            idx += 4

    return diagnostic_code

print(run(read_file("input.txt")))
