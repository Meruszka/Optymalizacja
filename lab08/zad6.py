import networkx as nx
import random

def get_degree(graph):
    degrees = []
    for i in range(len(graph)):
        degrees.append(0)
        for j in range(len(graph)):
            if graph[i][j] > 0:
                degrees[i] += 1
    return degrees

def make_graph_from_edges(ogGraph, edges: list):
    graph = ogGraph[:]
    for i in range(len(graph)):
        for j in range(len(graph)):
            graph[i][j] = 0
    for edge in edges:
        graph[edge[0]][edge[1]] = edge[2]
    return graph

def convert_to_nx(graph):
    nxgraph = nx.Graph()
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] > 0:
                nxgraph.add_edge(i, j, weight=graph[i][j])
    return nxgraph

def odd_vertices(edges):
    odd = []
    for edge in edges:
        if edge[0] not in odd:
            odd.append(edge[0])
        else:
            odd.remove(edge[0])
        if edge[1] not in odd:
            odd.append(edge[1])
        else:
            odd.remove(edge[1])
    return odd

def root(node, parent):
    while parent[node] != node:
        node = parent[node]
    return node

def sort_edges(graph):
    edges = []
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] > 0:
                if (j, i, graph[i][j]) not in edges:
                    edges.append((i, j, graph[i][j]))
    edges.sort(key=lambda x: x[2])
    return edges

def count_edges(graph):
    edges = 0
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] > 0:
                edges += 1
    return edges//2

def kruskal(graph):
    edges = sort_edges(graph)
    n = len(graph)
    parent = [i for i in range(n)]
    edges_in_tree = []
    i = 0
    while i < len(edges):
        edge = edges[i]
        if root(edge[0], parent) != root(edge[1], parent):
            edges_in_tree.append(edge)
            parent[root(edge[0], parent)] = root(edge[1], parent)
        i += 1
    return edges_in_tree

def isEulerian(graph):
    for i in range(len(graph)):
        if len(graph[i]) % 2 != 0:
            return False
    return True

def isSemiEulerian(graph):
    odd = 0
    for i in range(len(graph)):
        if len(graph[i]) % 2 != 0:
            odd += 1
    return odd == 2

def isFull(graph):
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] == 0 and i != j:
                return False
    return True

def fleury(graph):
    if not isEulerian(graph) and not isSemiEulerian(graph):
        print("Graph is not Eulerian or Semi-Eulerian")
        return None
    graph_copy = graph[:]
    degrees = get_degree(graph_copy)
    if isEulerian(graph_copy):
        current = 0
    else:
        for i in range(len(degrees)):
                if degrees[i] % 2 != 0:
                    current = i
                    break
    tour = [current]
    while len(tour) < count_edges(graph_copy):
        if degrees[current] == 1:
            for i in range(len(graph_copy[current])):
                if graph_copy[current][i] > 0:
                    tour.append(i)
                    
                    # remove edge
                    graph_copy[current][i] = 0
                    graph_copy[i][current] = 0
                    
                    # update degrees
                    degrees[current] -= 1
                    degrees[i] -= 1
                    current = i
                    break
        else:
            for i in range(len(graph_copy[current])):
                if graph_copy[current][i] > 0:
                    weight = graph_copy[current][i]
                    # remove edge
                    graph_copy[current][i] = 0
                    graph_copy[i][current] = 0
                    
                    # update degrees
                    degrees[current] -= 1
                    degrees[i] -= 1
                    
                    if isEulerian(graph_copy):
                        tour.append(i)
                        current = i
                        break
                    else:
                        # add edge
                        graph_copy[current][i] = weight
                        graph_copy[i][current] = weight
                        
                        # update degrees
                        degrees[current] += 1
                        degrees[i] += 1
                        
    return tour


def christofides(graph):
        if not isFull(graph):
            return None
        # get minimum spanning tree
        mst_edges = kruskal(graph)

        # form subgraph containing odd vertices
        oddGraph = make_graph_from_edges(graph, mst_edges)


        # get minimum weight perfect matching
        nxgraph = convert_to_nx(oddGraph)
        matching = nx.algorithms.min_weight_matching(nxgraph)

        # add edges from matching to minimum spanning tree
        for edge in matching:
            mst_edges.append((edge[0], edge[1], oddGraph[edge[0]][edge[1]]))
        
        # get eulerian tour
        tour = fleury(make_graph_from_edges(graph, mst_edges))

        # remove duplicate vertices
        if tour is not None:
            tour = list(dict.fromkeys(tour))
            return tour
        else:
            return 'Nie ma rozwiązania'

def create_random_graph(n):
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and graph[i][j] == 0:
                waga = random.randint(1, 10)
                graph[i][j] = waga
                graph[j][i] = waga
    return graph

def main():
    random.seed(0)
    print("Christofides algorithm:")
    print(christofides(create_random_graph(10)))

if __name__ == "__main__":
    main()