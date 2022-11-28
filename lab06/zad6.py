graph = [[0, 7, 0, 5, 0, 0, 0],
         [7, 0, 8, 9, 7, 0, 0],
         [0, 8, 0, 0, 5, 0, 0],
         [5, 9, 0, 0, 15, 6, 0],
         [0, 7, 5, 15, 0, 8, 9],
         [0, 0, 0, 6, 8, 0, 11],
         [0, 0, 0, 0, 9, 11, 0]]

graph2 = [[0, 8, 8, 3],
          [8, 0, 3, 7],
          [8, 3, 0, 6],
          [3, 7, 6, 0]]

graph3 = [[0, 3, 0, 0, 0, 4],
          [3, 0, 5, 0, 0, 8],
          [0, 5, 0, 5, 10, 14],
          [0, 0, 5, 0, 9, 0],
          [0, 0, 10, 9, 0, 6],
          [4, 8, 14, 0, 6, 0]]

graph4 = [[0, 1, 2, 3, 4],
          [1, 0, 5, 0, 0],
          [2, 5, 0, 0, 0],
          [3, 0, 0, 0, 6],
          [4, 0, 0, 6, 0]]


def sum_edges(graph):
    w_sum = 0
    l = len(graph)
    for i in range(l):
        for j in range(i, l):
            w_sum += graph[i][j]
    return w_sum


def dijktra(graph, source, dest):
    shortest = [0 for _ in range(len(graph))]
    selected = [source]
    l = len(graph)
    # Base case from source
    inf = 10000000
    min_sel = inf
    for i in range(l):
        # source to i
        if(i == source):
            # source to source
            shortest[source] = 0
        else:
            if(graph[source][i] == 0):
                shortest[i] = inf
            else:
                shortest[i] = graph[source][i]
                if(shortest[i] < min_sel):
                    min_sel = shortest[i]
                    ind = i

    if(source == dest):
        return 0
    # Dijktra's in Play
    selected.append(ind)
    while(ind != dest):
        for i in range(l):
            if i not in selected:
                if(graph[ind][i] != 0):
                    # Check if distance needs to be updated
                    if((graph[ind][i] + min_sel) < shortest[i]):
                        shortest[i] = graph[ind][i] + min_sel
        temp_min = 1000000

        for j in range(l):
            if j not in selected:
                if(shortest[j] < temp_min):
                    temp_min = shortest[j]
                    ind = j
        min_sel = temp_min
        selected.append(ind)

    return shortest[dest]

# Finding odd degree vertices in graph


def get_odd(graph):
    degrees = [0 for i in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph)):
            if(graph[i][j] != 0):
                degrees[i] += 1

    odds = [i for i in range(len(degrees)) if degrees[i] % 2 != 0]

    return odds

# Function to generate unique pairs


def gen_pairs(odds):
    pairs = []
    for i in range(len(odds)-1):
        pairs.append([])
        for j in range(i+1, len(odds)):
            pairs[i].append([odds[i], odds[j]])
    return pairs


def Chinese_Postman(graph):
    odds = get_odd(graph)
    path = []
    if(len(odds) == 0):
        for i in range(len(graph)):
            path.append(dijktra(graph, 0, i))
        return sum_edges(graph), "No odd degree vertices", path
    pairs = gen_pairs(odds)
    l = (len(pairs)+1)//2

    pairings_sum = []

    def get_pairs(pairs, done=[], final=[]):

        if(pairs[0][0][0] not in done):
            done.append(pairs[0][0][0])

            for i in pairs[0]:
                f = final[:]
                val = done[:]
                if(i[1] not in val):
                    f.append(i)
                else:
                    continue

                if(len(f) == l):
                    pairings_sum.append(f)
                    return
                else:
                    val.append(i[1])
                    get_pairs(pairs[1:], val, f)

        else:
            get_pairs(pairs[1:], done, final)

    get_pairs(pairs)
    min_sums = []
    for i in pairings_sum:
        s = 0
        for j in range(len(i)):
            s += dijktra(graph, i[j][0], i[j][1])
        min_sums.append(s)

    added_dis = min(min_sums)
    chinese_dis = added_dis + sum_edges(graph)
    return chinese_dis


print('Chinese Postman Distance is:', Chinese_Postman(graph))
print('Chinese Postman Distance is:', Chinese_Postman(graph2))
print('Chinese Postman Distance is:', Chinese_Postman(graph3))
print('Chinese Postman Distance is:', Chinese_Postman(graph4))
