import random
import csv
import configparser
import time
import networkx as nx
import matplotlib.pyplot as plt
import scipy as sp


config = configparser.ConfigParser()
config.read("config.ini")
t = int(config['Graph']['top'])
c = int(config['Graph']['max'])
fn = 'input_graph'
res=[[] * 1 for i in range(t)]

def create_file(filename, graff):
    file = open('{}.csv'.format(filename), 'w', newline='')
    write = csv.writer(file, delimiter = ',', quotechar = '"')
    for line in graff:
        write.writerow(line)
    file.close()

def draw_graph(filename):
    G = nx.DiGraph()
    with open('{}.csv'.format(filename), newline='') as csvfile:
        graph_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in graph_reader:
            node = int(row[0])
            neighbors = [int(n) for n in row[1:]]
            for neighbor in neighbors:
                G.add_edge(node, neighbor)
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)
    plt.show()

def oriented_graph(top, communicate, filename):
    f = []
    s = list(range(top))
    mass = []
    for i in range(top):
        mass.append(set())
    rand = random.choice(s)
    s.remove(rand)
    f.append(rand)
    while (s != []):
        rand = random.choice(s)
        rand1 = random.choice(f)
        mass[rand].add(rand1)
        s.remove(rand)
        f.append(rand)
    for i in range(top):
        if len(mass[i]) != 0:
            rand = random.randint(1, (communicate - 1))
        else:
            rand = random.randint(1, communicate)
        while len(mass[i]) < rand:
            new_edge = random.randint(0, top - 1)
            if new_edge != i and new_edge not in mass[i]:
                mass[i].add(new_edge)
    mass = [list(x) for x in mass]
    create_file(filename, mass)
    draw_graph(filename)
start = time.time()
oriented_graph(t,c,fn)
print(f'Программа сделана за {time.time() - start}')