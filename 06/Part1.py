def read_file(filename: str) -> list:
    with open(filename, "r") as f:
        line = f.readlines()
        return [i.strip("\n") for i in line]


def make_tree(data: list) -> dict:
    parents = {}
    for line in data:
        child, parent = line.split(")")
        parents[parent] = child
    return parents


class Orbit(object):

    def __init__(self, total_orbits=0):
        self.total_orbits = total_orbits

    def count_total_orbits(self, data: dict) -> str:
        total_orbits = 0
        for key in data.keys():
            while key in data:
                total_orbits += 1
                key = data[key]
        return str(total_orbits)


if __name__ == '__main__':
    tree = make_tree(read_file("input.txt"))
    orbit = Orbit()
    print("The total number of direct and indirect orbits: " + orbit.count_total_orbits(tree))
