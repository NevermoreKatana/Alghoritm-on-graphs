import csv
import sys
import time

sys.setrecursionlimit(10 ** 6)


def kosaraju(graph):
    visited = [False] * len(graph)
    stack = []
    def dfs1(n):
        visited[n] = True
        for neighbor in graph[n]:
            if not visited[neighbor]:
                dfs1(neighbor)
        stack.append(n)
    for node in range(len(graph)):
        if not visited[node]:
            dfs1(node)

    visited = [False] * len(graph)
    comp = []


    def dfs2(node, component):
        visited[node] = True
        component.append(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs2(neighbor, component)

    while stack:
        node = stack.pop()
        if not visited[node]:
            component = []
            dfs2(node, component)
            comp.append(component)

    return comp


def dffs3(graph, start):
    visited = [False] * len(graph)
    stack = [(start, 0)]
    while stack:
        node, d = stack.pop()
        if not visited[node]:
            visited[node] = True
            if d < 5:
                for neighbor in graph[node]:
                    stack.append((neighbor, d + 1))

    return visited


graph = []
start = time.time()
with open('input_graph.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        graph.append(list(map(int, row)))

components = []

for node in range(len(graph)):
    if not any(node in component for component in components):
        visited = dffs3(graph, node)
        if any(visited):
            kosaraju_result = kosaraju(graph)
            for c in kosaraju_result:
                if node in c:
                    components.append(c)
                    break
        else:
            components.append([node])

with open('output_graph1.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(components)
print(f'Выполнена за {time.time() - start}')