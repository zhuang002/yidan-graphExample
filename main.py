import copy
import sys


class ArrayGraph:
    def __init__(self):
        self.data = []
        self.paths = 0
        self.nodes = 0

    def read_graph_directional(self):
        nodes, paths = map(int, input().split(' '))
        self.nodes = nodes
        self.paths = paths
        self.data = [[0] * nodes for i in range(nodes)]
        for i in range(paths):
            start, end, length = map(int, input().split(' '))
            self.data[start][end] = length

    def read_graph_bidirectional(self):
        nodes, paths = map(int, input().split(' '))
        self.nodes = nodes
        self.paths = paths
        self.data = [[0] * nodes for i in range(nodes)]
        for i in range(paths):
            start, end, length = map(int, input().split(' '))
            self.data[start][end] = length
            self.data[end][start] = length

    def __str__(self):
        ret = ""
        ret += str(self.nodes) + " " + str(self.paths) + "\r\n"
        for i in range(self.nodes):
            for j in range(self.nodes):
                if self.data[i][j] != 0:
                    ret += str(i) + " " + str(j) + " " + str(self.data[i][j]) + "\r\n"
        return ret

    def get_shortest_node(self, list, distances):
        min = sys.maxsize
        min_node = None
        for node in list:
            if distances[node] < min:
                min = distances[node]
                min_node = node
        return min_node

    def get_neighbours(self, node):
        neighbours = []
        for i in range(self.nodes):
            if self.data[node][i]>0:
                neighbours.append(i)
        return neighbours


    def get_shortest_distance(self, node1, node2):
        completed = [False]*self.nodes
        distances = [-1]*self.nodes

        current = [node1]
        distances[node1] = 0
        while current:
            shortest_node = self.get_shortest_node(current, distances)
            neighbours = self.get_neighbours(shortest_node)
            for node in neighbours:
                if not completed[node]:
                    new_distance = distances[shortest_node]+self.data[shortest_node][node];
                    if distances[node] == -1:
                        distances[node] = new_distance
                    elif distances[node] > new_distance:
                        distances[node] = new_distance
                    current.append(node)
            current.remove(shortest_node)
            completed[shortest_node] = True
        return distances[node2]



class Path:
    def __init__(self, start,end, len):
        self.start = start
        self.end = end
        self.length = len


class Node:
    def __init__(self,id):
        self.id = id


class PathGraph:
    def __init__(self):
        self.all_nodes = None
        self.all_paths = None

    def read_graph_directional(self):
        nodes, paths = map(int, input().split(' '))
        self.all_nodes = [None] * nodes
        self.all_paths = [None] * paths

        for i in range(nodes):
            node = Node(i)
            self.all_nodes[i] = node

        for i in range(paths):
            start, end, length = map(int, input().split(' '))
            start_node = self.all_nodes[start]
            end_node = self.all_nodes[end]
            path = Path(start_node, end_node, length)
            self.all_paths[i] = path

    def __str__(self):
        ret = ""
        for path in self.all_paths:
            ret += "%d %d %d \r\n" % (path.start.id, path.end.id, path.length)
        return ret

    def getMinimumConstructTree(self):
        paths = copy.copy(self.all_paths)
        paths.sort(key=lambda x: x.length)

        subtree_set = []  # contains subtree. each subtree contains connected nodes

        construct_tree = PathGraph()
        construct_tree.all_nodes = []
        construct_tree.all_paths = []

        for path in paths:
            subtree1 = self.get_subtree_of_node(subtree_set, path.start)
            subtree2 = self.get_subtree_of_node(subtree_set, path.end)
            if subtree1:
                if subtree2:   # subtrees of both nodes are found.
                    if subtree1 != subtree2:
                        subtree_set.remove(subtree1)
                        subtree_set.remove(subtree2)
                        subtree_set.append(subtree1.union(subtree2))
                        construct_tree.all_paths.append(path)
                else:  # subtree1 is found, subtree2 is not found
                    subtree1.add(path.end.id)
                    construct_tree.all_paths.append(path)
                    construct_tree.all_nodes.append(path.end)
            else:
                if subtree2:  # subtree1 is not found, subtree2 is found
                    subtree2.add(path.start.id)
                    construct_tree.all_paths.append(path)
                    construct_tree.all_nodes.append(path.start)
                else:  # both subnodes are not found
                    subtree = {path.start.id, path.end.id}
                    subtree_set.append(subtree)
                    construct_tree.all_nodes.extend([path.start, path.end])
                    construct_tree.all_paths.append(path)
            if len(subtree_set) == 1 and len(construct_tree.all_nodes) == len(self.all_nodes):
                break

        construct_tree.all_nodes.extend(self.all_nodes)
        return construct_tree

    def get_subtree_of_node(self, subtree_set, node):
        for subtree in subtree_set:
            if node.id in subtree:
                return subtree
        return None


class Node1:
    def __init__(self, id):
        self.id = id
        self.toNodes = []


class NodeGraph:
    def __init__(self):
        self.nodes = None

    def read_graph_directional(self):
        nodes, paths = map(int, input().split(' '))
        self.nodes=[]
        for i in range(nodes):
            self.nodes.append(Node1(i))

        for i in range(paths):
            start, end, length = map(int, input().split(' '))
            start_node = self.nodes[start]
            end_node = self.nodes[end]
            start_node.toNodes.append((end_node, length))

    def __str__(self):
        ret = ""
        for node in self.nodes:
            for toNode in node.toNodes:
                ret += "%d %d %d\r\n" % (node.id, toNode[0], toNode[1])
        return ret


'''
graph = ArrayGraph()
graph.read_graph_directional()
print(graph)

graph = ArrayGraph()
graph.read_graph_bidirectional()
print(graph)

graph = PathGraph()
graph.read_graph_directional()
print(graph)

graph = NodeGraph()
graph.read_graph_directional()
print(graph)

graph = ArrayGraph()
graph.read_graph_bidirectional()
node1, node2 = map(int, input("Please input node1, node2:").split(' '))
distance = graph.get_shortest_distance(node1,node2)
print('Shortest distance:'+str(distance))
'''


graph = PathGraph()
graph.read_graph_directional()
tree = graph.getMinimumConstructTree()
print(tree)

