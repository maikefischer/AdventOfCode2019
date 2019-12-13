def read_file(filename):
    with open(filename) as f:
        content = f.readlines()
        content = content[0].strip().split(',')
        content = [int(x) for x in content]
        f.close()
    return content


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def operation(list_all):
    idx = 0

    while list_all[idx] != 99:

        position_output = list_all[idx + 3]
        value_for_x = list_all[list_all[idx + 1]]
        value_for_y = list_all[list_all[idx + 2]]

        if list_all[idx] == 1:
            value_for_output = add(value_for_x, value_for_y)
        elif list_all[idx] == 2:
            value_for_output = multiply(value_for_x, value_for_y)

        idx += 4
        list_all[position_output] = value_for_output

    return list_all

print(operation(read_file("input.txt"))) #4090701

