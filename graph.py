class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node, weight=0):
        if node not in self.graph:
            self.graph[node] = {'weight': weight, 'edges': {}}

    def add_edge(self, node1, node2, weight):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1]['edges'][node2] = weight
            self.graph[node2]['edges'][node1] = weight
        else:
            print("One or both nodes are not present in the graph")