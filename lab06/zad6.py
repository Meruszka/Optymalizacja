def isEulerian(G):
    n = len(G)
    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                return True
    return False

def EulerianCycle(G):
    print("Eulerian cycle")
    n = len(G)
    if not isEulerian(G):
        return None
    start = 0
    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                start = i
                break
    cycle = [start]
    while len(cycle) < n:
        for i in range(n):
            if G[cycle[-1]][i] != 0:
                cycle.append(i)
                G[cycle[-2]][i] = 0
                G[i][cycle[-2]] = 0
                break
    return cycle

def EulerianPath(G):
    print("Eulerian path")
    n = len(G)
    if not isEulerian(G):
        return None
    start = 0
    end = 0
    for i in range(n):
        suma = 0
        for j in range(n):
            suma += G[i][j]
        if suma % 2 == 1:
            start = i
        suma = 0
        for j in range(n):
            suma += G[j][i]
        if suma % 2 == 1:
            end = i
    G[start][end] += 1
    G[end][start] += 1
    cycle = EulerianCycle(G)
    for i in range(len(cycle)):
        if cycle[i] == start and cycle[i+1] == end:
            return cycle[i+1:] + cycle[1:i+1]
    return None

def ChooseAlgorithm(G):
    if isEulerian(G):
        return EulerianCycle(G)
    else:
        return EulerianPath(G)

def test():
    graf = [[0, 7, 0, 5, 0, 0, 0],
            [7, 0, 8, 9, 7, 0, 0],
            [0, 8, 0, 0, 5, 0, 0],
            [5, 9, 0, 0, 15, 6, 0],
            [0, 7, 5, 15, 0, 8, 9],
            [0, 0, 0, 6, 8, 0, 11],
            [0, 0, 0, 0, 9, 11, 0]]

    print(ChooseAlgorithm(graf))


def main():
    test()


if __name__ == '__main__':
    main()