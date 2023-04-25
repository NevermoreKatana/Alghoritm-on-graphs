import random
import time


def generate_graph(num_vertices_left, num_vertices_right, max_weight):
    graph = {}
    for i in range(num_vertices_left):
        graph[i] = {}
        for j in range(num_vertices_left, num_vertices_left + num_vertices_right):
            graph[i][j] = random.randint(1, max_weight)
            graph[j] = {}
    return graph


def graph_to_file(graph, filename):
    with open(filename, "w") as file:
        for i in graph:
            for j in graph[i]:
                file.write(f"{i} {j} {graph[i][j]}\n")


def graph_to_matrix(graph, num_vertices_left, num_vertices_right):
    matrix = []
    for i in range(num_vertices_left):
        row = []
        for j in range(num_vertices_left, num_vertices_left + num_vertices_right):
            row.append(graph[i][j])
        matrix.append(row)
    return matrix

def matrix_to_file(matrix, filename):
    with open(filename, "w") as file:
        for row in matrix:
            file.write(" ".join(str(x) for x in row) + "\n")

start = time.time()

num_vertices_left = 10000
num_vertices_right = 2000
max_weight = 10

graph = generate_graph(num_vertices_left, num_vertices_right, max_weight)
graph_to_file(graph, "bipartite graph.txt")

matrix = graph_to_matrix(graph, num_vertices_left, num_vertices_right)
matrix_to_file(matrix, "matrix.txt")

print(time.time()-start)
