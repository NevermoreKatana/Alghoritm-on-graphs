# Графы и транспортные сети: Реализации алгоритмов

## Описание
Данный репозиторий содержит реализации различных алгоритмов на графах и транспортных сетях. Здесь вы найдете генератор ориентированных и неориентированных графов, реализации поиска в глубину и ширину, алгоритм Краскала для построения минимального остовного дерева, алгоритм Косараджу для выделения максимальной связной компоненты, алгоритм Диница для поиска максимального потока в транспортной сети и алгоритм Венгерского для поиска максимального паросочетания в двудольном графе.

# 1. Генератор графов
Генерирует граф разной связности. На входе программы данные из config.ini, а именно максимальное количество вершин и максимальное количество связей у каждой вершины. Результат выводится в CSV файле, представленном в виде списка смежности.

# 2. Поиск в глубину и ширину
На вход программы подается CSV файл с графом, записанным в виде списка смежности. На выходе в консоль выводится конечная связь для BFS и DFS.

## BFS
![BFS Animation](https://upload.wikimedia.org/wikipedia/commons/5/5d/Breadth-First-Search-Algorithm.gif)
## DFS
![DFS Animation](https://upload.wikimedia.org/wikipedia/commons/7/7f/Depth-First-Search.gif)

# 3. Алгоритм Краскала
На вход программы поступает CSV файл со списками смежности графа. Результатом работы являются связи для минимального остовного дерева.

![Алгоритм Краскала](https://media.proglib.io/posts/2020/09/08/574ff16387ff1b2ec365db1c75fa7ce4.gif)

# 4. Алгоритм Косараджу
На вход программы поступает CSV файл со списками смежности. Результатом работы являются списки смежностей максимальной связной компоненты.

![Алгоритм Косараджу](https://media.proglib.io/wp-uploads/-000//1/597791923c2e0_UvC39m2.gif)

# 5. Алгоритм Диница
На вход программы поступает CSV файл со списками смежности транспортной сети. Результатом является значение максимального потока в сети.

![Алгоритм Диница](https://media.proglib.io/posts/2020/09/08/06c0a8bbb4502b55e1b4707e397bc7f4.gif)


# 5. Венгерский Алгоритм
Реализация Венгерского алгоритма для поиска максимального паросочетания в двудольном графе.  В программу на вход поступает матрица транспортной сети, на выходе программа выдает значение максимального паросочетания


# Graphs and Transport networks: Algorithm Implementations

## Description
This repository contains implementations of various algorithms on graphs and transport networks. Here you will find a generator of oriented and undirected graphs, implementations of depth and width search, Kraskal's algorithm for constructing a minimum spanning tree, Kosaraju's algorithm for allocating the maximum connected component, Dinitz's algorithm for finding the maximum flow in the transport network and Hungarian's algorithm for finding the maximum matching in a bipartite graph.

# 1. Graph generator
Generates a graph of different connectivity. At the input of the program, the data from config.ini, namely the maximum number of vertices and the maximum number of connections for each vertex. The result is output in a CSV file, presented as an adjacency list.

# 2. Search in depth and width
A CSV file with a graph written as an adjacency list is submitted to the program input. The final link for BFS and DFS is output to the console.

![BFS Animation](https://upload.wikimedia.org/wikipedia/commons/5/5d/Breadth-First-Search-Algorithm.gif)
# DFS
![DFS Animation](https://upload.wikimedia.org/wikipedia/commons/7/7f/Depth-First-Search.gif)

# 3. Kraskal's algorithm
The program receives a CSV file with the adjacency lists of the graph. The result of the work are connections for a minimal spanning tree.

![Алгоритм Краскала](https://media.proglib.io/posts/2020/09/08/574ff16387ff1b2ec365db1c75fa7ce4.gif)


# 4. Kosaraju Algorithm
A CSV file with adjacency lists is received at the input of the program. The result of the work are lists of adjacencies of the maximum connected component.

![Алгоритм Косараджу](https://media.proglib.io/wp-uploads/-000//1/597791923c2e0_UvC39m2.gif)

# 5. The Dinitz algorithm
A CSV file with lists of transport network adjacency is received at the input of the program. The result is the value of the maximum flow in the network.

![Алгоритм Диница](https://media.proglib.io/posts/2020/09/08/06c0a8bbb4502b55e1b4707e397bc7f4.gif)

# 5. Hungarian Algorithm
Implementation of the Hungarian algorithm for finding the maximum match in a bipartite graph.  The program receives a matrix of the transport network at the input, at the output the program outputs the value of the maximum match
