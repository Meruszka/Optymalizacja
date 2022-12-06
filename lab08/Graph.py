import copy
import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, size, adjacency_matrix=None):
        if adjacency_matrix is None:
            adjacency_matrix = [[[] for _ in range(size)] for _ in range(size)]
        self.adjacency_matrix = adjacency_matrix

    def convert_to_networkx(self):
        g = nx.Graph()
        for i in range(len(self.adjacency_matrix)):
            for j in range(len(self.adjacency_matrix)):
                if self.adjacency_matrix[i][j]:
                    g.add_edge(i, j, weight=self.adjacency_matrix[i][j][-1])
        return g

    def visualize(self):
        g = nx.Graph()
        for i in range(len(self.adjacency_matrix)):
            for j in range(len(self.adjacency_matrix)):
                if self.adjacency_matrix[i][j]:
                    g.add_edge(i, j, weight=self.adjacency_matrix[i][j][-1])
        nx.draw(g, with_labels=True)
        edge_labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos=nx.spring_layout(g), edge_labels=edge_labels)
        plt.show()

    def add_edge(self, u, v, weight):
        self.adjacency_matrix[u][v].append(weight)
        self.adjacency_matrix[v][u].append(weight)

    def remove_edge(self, u, v):
        self.adjacency_matrix[u][v].pop()
        self.adjacency_matrix[v][u].pop()

    def remove_vertex(self, vertex):
        for i in range(len(self.adjacency_matrix)):
            self.adjacency_matrix[vertex][i] = []
            self.adjacency_matrix[i][vertex] = []

    def get_degree(self, vertex):
        degrees = 0
        for i in range(len(self.adjacency_matrix)):
            if self.adjacency_matrix[vertex][i]:
                degrees += len(self.adjacency_matrix[vertex][i])
        return degrees

    def _min_key(self, weights, visited):
        min = float('inf')
        min_index = None
        for v in range(len(self.adjacency_matrix)):
            if weights[v] < min and v not in visited:
                min = weights[v]
                min_index = v
        return min_index

    def mst(self):
        # prim's algorithm
        num_vertices = len(self.adjacency_matrix)
        mst = Graph(num_vertices)

        visited = []

        weights = [float('inf') for _ in range(num_vertices)]
        weights[0] = 0

        parent = [None for _ in range(num_vertices)]
        parent[0] = -1

        for _ in range(num_vertices):
            u = self._min_key(weights, visited)
            visited.append(u)
            for v in range(num_vertices):
                if self.adjacency_matrix[u][v] and v not in visited and weights[v] > self.adjacency_matrix[u][v][-1]:
                    weights[v] = self.adjacency_matrix[u][v][-1]
                    parent[v] = u
        for i in range(1, num_vertices):
            mst.add_edge(parent[i], i, weights[i])
        return mst

    def is_eulerian(self):
        # get degrees of all vertices
        degrees = [self.get_degree(i) for i in range(len(self.adjacency_matrix))]
        # if all degrees are even, graph is eulerian
        return all([degree % 2 == 0 for degree in degrees])

    def is_semi_eulerian(self):
        # get degrees of all vertices
        degrees = [self.get_degree(i) for i in range(len(self.adjacency_matrix))]
        # if all degrees are even, graph is eulerian
        return all([degree % 2 == 0 for degree in degrees])

    def dfs_count(self, v, visited):
        visited[v] = True
        count = 1
        for i in range(len(self.adjacency_matrix)):
            if self.adjacency_matrix[v][i] and not visited[i]:
                count += self.dfs_count(i, visited)
        return count

    def count_edges(self):
        count = 0
        for i in range(len(self.adjacency_matrix)):
            for j in range(len(self.adjacency_matrix)):
                if self.adjacency_matrix[i][j]:
                    count += len(self.adjacency_matrix[i][j])
        return count//2

    def fleury(self):
        if not self.is_eulerian() and not self.is_semieulerian():
            return None
        adjCopy = copy.deepcopy(self.adjacency_matrix)
        graph = Graph(len(self.adjacency_matrix), adjCopy)
        degrees = [graph.get_degree(i) for i in range(len(self.adjacency_matrix))]
        if graph.is_eulerian():
            current = 0
        else:
            for i in range(len(degrees)):
                if degrees[i] % 2 != 0:
                    current = i
                    break
        path = [current]
        edges_count = graph.count_edges()
        while len(path) <= edges_count:
            if degrees[current] == 1:
                for i in range(len(graph.adjacency_matrix[current])):
                    if len(graph.adjacency_matrix[current][i]) != 0:
                        graph.remove_edge(current, i)
                        path.append(i)
                        degrees[current] -= 1
                        degrees[i] -= 1
                        current = i
                        break
            else:
                for i in range(len(graph.adjacency_matrix[current])):
                    if len(graph.adjacency_matrix[current][i]) != 0:
                        if degrees[i] != 1:
                            dfs_count = graph.dfs_count(i, [False] * len(graph.adjacency_matrix))
                            weight = graph.adjacency_matrix[current][i][0]
                            graph.remove_edge(current, i)

                            dfs_count_after = graph.dfs_count(i, [False] * len(graph.adjacency_matrix))

                            if dfs_count_after == dfs_count:
                                path.append(i)
                                degrees[current] -= 1
                                degrees[i] -= 1
                                current = i
                                break
                            else:
                                graph.add_edge(current, i, weight)
        return path

    def christofides(self):
        # get mst
        mst = self.mst()

        # get odd vertices
        degrees = [mst.get_degree(i) for i in range(len(mst.adjacency_matrix))]
        odd_vertices = [i for i in range(len(degrees)) if degrees[i] % 2 == 1]

        # form subgraph containing odd vertices
        oddGraph = Graph(len(self.adjacency_matrix))
        for i in odd_vertices:
            for j in odd_vertices[odd_vertices.index(i) + 1:]:
                oddGraph.add_edge(i, j, self.adjacency_matrix[i][j][0])

        # get minimum weight perfect matching
        nxgraph = oddGraph.convert_to_networkx()
        matching = nx.algorithms.min_weight_matching(nxgraph)

        # add edges from matching to mst
        for edge in matching:
            mst.add_edge(edge[0], edge[1], oddGraph.adjacency_matrix[edge[0]][edge[1]][0])
        
        # get eulerian tour
        tour = mst.fleury()

        # remove duplicate vertices
        tour = list(dict.fromkeys(tour))

        return tour

