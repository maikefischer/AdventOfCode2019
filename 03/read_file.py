def read_line1(filename):
    with open(filename) as f:
        line1 = f.readline().strip().split(",")
        return line1


def read_line2(filename):
    with open(filename) as f:
        line1 = f.readline().strip().split(",")
        line2 = f.readline().strip().split(",")
        return line2
