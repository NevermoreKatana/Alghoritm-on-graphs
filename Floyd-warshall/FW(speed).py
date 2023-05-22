import time
from generator import generator
import numpy as np
from numba import njit, prange
import configparser


config = configparser.ConfigParser()
config.read("cfg.ini")

@njit(parallel=True, nogil=True)
def floyd_warshall(adj_matrix):
    n = adj_matrix.shape[0]
    dist = adj_matrix.copy()
    path = np.zeros((n, n), dtype=np.int64)
    for k in prange(n):
        for i in prange(n):
            for j in prange(n):
                if dist[i, j] > dist[i, k] + dist[k, j]:
                    dist[i, j] = dist[i, k] + dist[k, j]
                    path[i, j] = k

    return dist, path

def read_graph(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        adj_list = []
        for line in lines:
            values = list(map(int, line.strip().split(';')))
            adj_list.append(values)
    return adj_list

def graph_conversion(adj_list):
    n = len(adj_list)
    adj_matrix = np.full((n, n), np.inf, dtype=np.float64)
    for i in range(n):
        for j in range(0, len(adj_list[i]), 2):
            neighbor = adj_list[i][j]
            weight = adj_list[i][j + 1]
            adj_matrix[i, neighbor] = weight
    np.fill_diagonal(adj_matrix, 0)
    return adj_matrix

generator().g2()
startFW = time.time()

def floyd_warshall_from_csv(file_path):
    adj_list = read_graph(file_path)
    adj_matrix = graph_conversion(adj_list)
    dist, path = floyd_warshall(adj_matrix)
    return dist, path

csv_file_path = f'{config["settings"]["filename"]}.csv'
distances, path = floyd_warshall_from_csv(csv_file_path)
stopFW = time.time()-startFW
#startPR = time.time()

n = len(distances)
for i in range(n):
    for j in range(n):
        if distances[i, j] == np.inf:
            print(f"Кратчайший путь из {i} в {j}: Пути нет")
        else:
            print(f"Кратчайший путь из {i} в {j}: {distances[i, j]}")
        if path[i, j] != 0:
            print(f"Путь: {i} -> {path[i, j]} -> {j}")
        else:
            print(f"Путь: {i} -> {j}")
#stopPR = time.time()-startPR
print(f"The algorithm completed in {stopFW} seconds")
#print(f"Print completed in {stopPR} seconds")
