from Graf import *

g = [[0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]]

def DFS(macierz, start):
    st = [start]
    visited = [start]
    while True:
        if len(st) == 0:
            break
        v = st.pop()
        print(v)
        for i in range(len(macierz)):
            if macierz[v][i] == 1 and i not in visited:
                st.append(i)
                visited.append(i)
    print(visited)

DFS(g, 0)