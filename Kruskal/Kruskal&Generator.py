import random
import heapq
import csv
import configparser


cfg = configparser.ConfigParser()
cfg.read("config.ini")
n = int(cfg['Graph']['top'])
max_conn = int(cfg['Graph']['max'])

def generate_graph(v, conns):
    l = [[] for _ in range(v)]
    for i in range(v):
        for j in range(i + 1, v):
            if len(l[i]) < conns and len(l[j]) < conns:
                weight = random.randint(1, 10)
                l[i].append((j, weight))
                l[j].append((i, weight))
    with open("input_graph.csv", "w", newline="") as f:
        write = csv.writer(f)
        for i in range(v):
            row = [str(i)]
            for j, weight in l[i]:
                row.append(str(j) + "," + str(weight))
            write.writerow(row)
    return l


def find(p, i):
    if p[i] == i:
        return i
    return find(p, p[i])


def union(p, s, x, y):
    xr = find(p, x)
    yr = find(p, y)
    if xr == yr:
        return
    if s[xr] < s[yr]:
        xr, yr = yr, xr
    p[yr] = xr
    s[xr] += s[yr]


def kruskal(l):
    v = len(l)
    edges = []
    for i in range(v):
        for j, weight in l[i]:
            edges.append((weight, i, j))
    edges.sort()
    parents = [i for i in range(v)]
    si = [1] * v
    result = [[] for _ in range(v)]
    for weight, u, v in edges:
        if find(parents, u) != find(parents, v):
            union(parents, si, u, v)
            result[u].append((v, weight))
            result[v].append((u, weight))

    return result
l = generate_graph(n, max_conn)
krusk_tree = kruskal(l)

with open("output_graph.csv", "w", newline="") as f:
    write = csv.writer(f)
    for i in range(len(krusk_tree)):
        row = [str(i)]
        for j, weight in krusk_tree[i]:
            row.append(str(j) + "," + str(weight))
        write.writerow(row)
