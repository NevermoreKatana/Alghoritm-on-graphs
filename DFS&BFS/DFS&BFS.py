import csv
import time


with open('test.csv', 'r') as file:
    f = csv.reader(file, delimiter = ';')
    i=0
    for row in f:
        i +=1


vertexes = i

def for_dfs():
    graph = {}
    mass = []
    with open('test.csv', 'r') as file:
        f = csv.reader(file, delimiter=',')
        for row in f:
            mass.append(row)
        for index in range(0, vertexes):
            massive = []
            for j in range(len(mass[index])):
                ch = mass[index][j]
                massive.append(int(ch))
            graph[index+1] = massive
    return graph

def for_bfs():
    graph = {}
    with open('test.csv', 'r') as file:
        f = csv.reader(file, delimiter=',')
        massive = []
        for row in f:
            massive.append(row)
    for index in range(0, vertexes):
        graph[f'{index+1}'] = massive[index]
    return graph


def dfs(graph,start):
    res = []
    visited = [start]
    stack = [start]
    while len(stack) != 0:
        v = stack.pop()
        res.append(v)
        srt = graph[v]
        srt = list(filter((lambda sr:sr not in visited),srt))
        visited.extend(srt)
        for sr in srt:
            stack.append(sr)
    return res


def bfs(graph, start, visited = None):
    finaly = []
    res = []
    visited = []
    visited.append(start)
    res.append(start)
    while res:
        s = res.pop(0)
        finaly.append(int(s))
        for i in graph[s]:
            if i not in visited:
                visited.append(i)
                res.append(i)
    return finaly
full_time = time.time()
st_dfs = time.time()
print('DFS:')
print(dfs(for_dfs(), 1))
print(f"DFS was completed in {time.time() - st_dfs} seconds.")
st_bfs = time.time()
print('\nBFS:')
print(bfs(for_bfs(),'1'))
print(f"BFS was completed in {time.time() - st_bfs} seconds.")
print(f"\nFULL was completed in {time.time() - full_time} seconds.")