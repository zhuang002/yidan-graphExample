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
            self.all_paths.append(path)

    def __str__(self):
        ret = ""
        for i in range(self.all_paths):
            ret += "%d %d %d \r\n" % (self.all_paths[i].start, self.all_paths[i].end, self.all_paths[i].length)
        return ret


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
