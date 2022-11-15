import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


random.seed(0)
graph = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 1, 1, 0, 1, 1, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 1, 0, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]


def sort_edges(graph):
    edges = []
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] > 0:
                if (j, i, graph[i][j]) not in edges:
                    edges.append((i, j, graph[i][j]))
    edges.sort(key=lambda x: x[2])
    return edges

def set_random_weights(graph):
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] > 0:
                graph[i][j] = random.randint(1, 10)
                graph[j][i] = graph[i][j]
    return graph

def root(node, parent):
    while parent[node] != node:
        node = parent[node]
    return node

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
    return edges_in_tree, sum([edge[2] for edge in edges_in_tree])

def print_graph(graph):
    for i in range(len(graph)):
        for j in range(len(graph)):
            print(graph[i][j], end=" ")
        print()

g = set_random_weights(graph)
edges, suma = kruskal(g)
print_graph(g)

print(edges)
print(suma)
G = nx.from_numpy_matrix(np.matrix(g), create_using=nx.Graph)
layout = nx.spring_layout(G)
nx.draw(G, layout, with_labels=True)
nx.draw_networkx_edge_labels(G, layout)
plt.show()

X = nx.Graph()
for edge in edges:
    X.add_edge(edge[0], edge[1], weight=edge[2])
layout1 = nx.spring_layout(X)
nx.draw(X, with_labels=True)
nx.draw_networkx_edge_labels(X, layout1)
plt.show()


    
