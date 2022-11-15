import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

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


def dfs(graph, start, visited=None, path=[], edges=[]):
    if visited is None:
        visited = set()
    visited.add(start)
    path.append(start)
    for next in range(len(graph[start])):
        if graph[start][next] and next not in visited:
            edges.append((start, next))
            dfs(graph, next, visited, path, edges)

    return visited, path, edges


def print_graph(graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            print(graph[i][j], end=" ")
        print()


x = dfs(graph, 0)
print("Path: ", x[1])
print("Edges: ", x[2])

T = nx.from_numpy_matrix(np.matrix(graph))
nx.draw(T, with_labels=True)
plt.show()

G = nx.Graph()
G.add_edges_from(x[2])
nx.draw(G, with_labels=True)
plt.show()
