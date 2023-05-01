from math import inf
import csv
import configparser
from generator import generator

generator().g2()
config = configparser.ConfigParser()
config.read("cfg.ini")

def decstra(G, N):
    phi = {}
    for v in G.keys():
        phi[v] = inf
    phi[0] = 0
    marked = [0]
    while N - 1 not in marked:
        inc = []
        for i in marked:
            inc.extend([[i, k[0], k[1], phi[i] + k[1]] for k in G[i] if k[0] not in marked])
        protent = [a[3] for a in inc]
        min_phi = min(protent)
        vert = inc[(protent.index(min_phi))][1]
        phi[vert] = min_phi
        if vert not in marked:
            marked.append(vert)
            if vert == N - 1:
                break
    marked = [i for i in range(N)]
    inc = []
    for i in marked:
        inc.extend([[i, k[0], k[1]] for k in G[i]])
    result = proverka(phi, inc)
    if result == -1:
        return (-1, "Граф имеет отрицательный цикл")
    sum = phi[N - 1]
    path = []
    current = N - 1
    while current != 0:
        for r in pev(G, current):
            if phi[r[0]] + r[2] == phi[current]:
                path.append(current)
                current = r[0]
    path.append(0)
    path.reverse()
    return (sum, path)


def proverka(phi2, inc):
    for i in range(N - 1):
        for u, v, w in inc:
            if phi2[u] != float("Inf") and phi2[u] + w < phi2[v]:
                phi2[v] = phi2[u] + w
    for u, v, w in inc:
        if phi2[u] != float("Inf") and phi2[u] + w < phi2[v]:
            return -1


def pev(g, v):
    ret = []
    for k in g.keys():
        for e in g[k]:
            if e[0] == v:
                ret.append([k, e[0], e[1]])
    return ret


if __name__ == '__main__':
    G = {}
    file = config["settings"]["filename"]
    N = int(config["settings"]["top"])
    for i in range(N):
        G[i] = []
    T = []
    j = 0

    with open('{}.csv'.format(file), newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            d = row
            T.append([])
            d = d[0]
            q = ''
            for i in range(len(str(d))):
                if d[i] != ';':
                    q = q + d[i]
                    if i == len(str(d)) - 1:
                        T[j].append(q)
                else:
                    if d[i] == ';':
                        T[j].append(q)
                        q = ''
            j += 1
        c = 0
        r = 0
        while c < len(T):
            for i in range(len(T[c])):
                if i < len(T[c]) - r:
                    G[int(c)].append((int(T[c][i + r]), int(T[c][i + 1 + r])))
                    r = i + 1
            c += 1
            r = 0

    sum, path = decstra(G, N)

    if sum == -1:
        print(path)
    else:
        print("Длина кратчайшего пути:", sum)
        for i in range(len(path)):
            if i == len(path) - 1:
                print("%d" % path[i], end="")
                break
            print("%d -> " % path[i], end="")
    print(" ")
