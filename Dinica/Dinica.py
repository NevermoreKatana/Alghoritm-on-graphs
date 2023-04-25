import csv
import configparser
import time


def read_config():
    cfg = configparser.ConfigParser()
    cfg.read('config.ini')
    return int(cfg['Graph']['top'])


def create_graph(N):
    g = [[0] * N for _ in range(N)]
    return g


def read_file():
    T = []
    with open('input_transport_network.csv', newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            R = row[0].split(";")
            T.append([(int(R[i]), int(R[i+1])) for i in range(0, len(R), 2)])
    return T


def bfs(s, t, sub, g):
    visited = [False] * len(g)
    a = []
    a.append(s)
    visited[s] = True
    while a:
        u = a.pop(0)
        for key, val in enumerate(g[u]):
            if not visited[key] and val > 0:
                a.append(key)
                visited[key] = True
                sub[key] = u
    return True if visited[t] else False


def dinic(start, end, g):
    sub = [-1] * len(g)
    maxflow = 0
    while bfs(start, end, sub, g):
        value = float("inf")
        s = end
        way = [s]
        while s != start:
            value = min(value, g[sub[s]][s])
            s = sub[s]
            way.append(s)
        way.reverse()
        print(f"Way >> {way} << flow: {value}")
        maxflow += value
        en = end
        while en != start:
            u = sub[en]
            g[u][en] -= value
            g[en][u] += value
            en = sub[en]
    return maxflow


def main():
    start_time = time.time()
    N = read_config()
    g = create_graph(N)
    T = read_file()
    for i in range(N):
        for j, val in T[i]:
            g[i][j] += val
    s = 0
    t = N - 1
    result = dinic(s, t, g)
    print(f"Max flow >>> {result}")
    print(f"Program was completed by {time.time() - start_time}")


if __name__ == "__main__":
    main()