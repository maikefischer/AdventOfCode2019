import math


def read_file(filename):
    with open(filename) as f:
        content = f.readlines()
         #remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content]
        f.close()
    return content


def find_fuel(number):
    divideby3 = number/3
    rounddown = math.floor(divideby3)
    subtract = rounddown-2
    if subtract > 0:
        return int(subtract)
    return 0


def find_further_fuel(number):
    total = 0
    while number > 0:
        number = find_fuel(number)
        total += number
    return total


def find_total_fuel(data):
    data = read_file(data)
    fuel = [find_further_fuel(int(x)) for x in data]
    return sum(fuel)


print(find_total_fuel("input.txt"))
