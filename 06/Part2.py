import networkx as nx
from Part1 import read_file


def make_tree(data: list) -> dict:
	parents = {}
	for line in data:
		child, parent = line.split(")")
		parents[parent] = [child]
	return parents


class Orbit(object):

	def __init__(self, shortest_path=0):
		self.shortest_path = shortest_path

	def find_shortest_path(self, data: dict, start: str, end: str) -> str:
		graph = nx.Graph(data)
		return str(nx.shortest_path_length(graph, start, end) - 2)


if __name__ == '__main__':
    tree = make_tree(read_file("input.txt"))
    orbit = Orbit()
    print("The shortest path between YOU and SAN is: " + orbit.find_shortest_path(tree, "YOU", "SAN") + " orbits")
