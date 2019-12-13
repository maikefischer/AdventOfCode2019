def read_file(filename):
    with open(filename, "r") as f:
        line = f.readlines()
        return [i.strip("\n") for i in line]


def count_direct_orbits(data):
    return len(data)


def make_tree(data):
    parents = {}
    for line in data:
        child, parent = line.split(")")
        parents[parent] = [child]
    print(parents)
    return parents


def count_children(data):
    parents = make_tree(data)

    direct_orbits = 0

    for key in parents:
        value_1 = parents.get(key)
        direct_orbits += 1

        key = value_1


# def count_total_orbits():
#     return count_direct_orbits(data) + count_indirect_orbits(data)


data = read_file("input.txt")

print("The amount of direct orbits", count_direct_orbits(data))
print("The amount of indirect orbits", count_children(data))
# print("The amount of direct orbits", count_total_orbits())
