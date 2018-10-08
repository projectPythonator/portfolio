import time
from math import log10

import queue  
from collections import namedtuple

Edge = namedtuple('Edge', ['vertex', 'weight'])
nodes_dict = {}
grid = []

gra =None

'''makes a directed graph'''
class graph_dir_wgt(object):  
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.adjacency_list = [[] for _ in range(vertex_count)]

    def add_edge(self, source, dest, weight):
        assert source < self.vertex_count
        self.adjacency_list[source].append(Edge(dest, weight))

    def get_edge(self, vertex):
        for e in self.adjacency_list[vertex]:
            yield e

    def get_vertex(self):
        for v in range(self.vertex_count):
            yield v
    
    def print_graph(self):
        for i in self.adjacency_list:
            print(i)

'''combination of a book implementation and one i found online'''
def dijkstra(source, dest):
    start_weight = float("inf")
    q = queue.PriorityQueue()
    dist = [0 if i == source else start_weight for i in gra.get_vertex()]
    #par = [None]*len(dist)

    q.put(([0, source]))
    while not q.empty():
        v_tuple = q.get()
        d = v_tuple[0]
        v = v_tuple[1]
        if d > dist[v]:
            continue
        for e in gra.get_edge(v):
            candidate_distance = dist[v] + e.weight
            if dist[e.vertex] > candidate_distance:
                dist[e.vertex] = candidate_distance
                #par[e.vertex] = v
                q.put(([dist[e.vertex], e.vertex]))
    '''
    shortest_path = []
    end = dest
    while end is not None:
        shortest_path.append(end)
        end = par[end]
    '''
    return dist[dest]

def read_in_grid(name_file):
    global grid, nodes_dict
    grid = [[int(num) for num in line.split(',')] for line in open(name_file).readlines()]
    ind = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            nodes_dict[(i, j)] = ind
            ind += 1

def build_graph(leno):
    lim = len(grid)-1
    g = graph_dir_wgt(leno)
    for i in range(lim+1):
        for j in range(lim+1):
            if j < lim:
                g.add_edge(nodes_dict[(i, j)], nodes_dict[(i, j+1)], grid[i][j+1])
            if i < lim:
                g.add_edge(nodes_dict[(i, j)], nodes_dict[(i+1, j)], grid[i+1][j])
            if i > 0:
                g.add_edge(nodes_dict[(i, j)], nodes_dict[(i-1, j)], grid[i-1][j])
    return g



def sol1(name_file):
    global gra
    ans = 2**1000
    a = time.clock()
    read_in_grid(name_file)
    b = time.clock()
    print('time taken is {:f}'.format(b-a))
    a = time.clock()
    g = build_graph(len(grid)**2)
    gra = g
    b = time.clock()
    print('time taken is {:f}'.format(b-a))
    a = time.clock()
    for i in range(len(grid)):
        print(i)
        for j in range(len(grid)):
            cost = dijkstra(nodes_dict[(i, 0)], nodes_dict[(j, len(grid)-1)])
            if cost+grid[i][0] < ans:
                ans = cost+grid[i][0]
    b = time.clock()
    print('time taken is {:f}'.format(b-a))
    print('the min cost sum to traverse the grid is {}'.format(ans))


def main():
    name_file = 'in.txt'
    a = time.clock()
    sol1(name_file)
    b = time.clock()
    print('time taken is {:f}'.format(b-a))
main()
