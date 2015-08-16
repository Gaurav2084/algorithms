# Algorithms: Design and Analysis Part 1
# Stanford University

# Programming Question 4
# Strongly Connected Components (Compute Largest 5)
# Depth-First Search SCC for directed graph
# Kosaraju's Two-Pass Algorithm

import urllib2
import sys

# globals
SCC_URL = "http://spark-public.s3.amazonaws.com/algo1/programming_prob/SCC.txt"
SCC_LOCAL = "/Users/Hyperion/Desktop/SCC.txt"
TIME = 0 # finishing times for nodes, first pass
FTIMES = {} # associated leaders and finishing times
EXPLORED = [] # explored nodes
LEADERS = {} # leaders for nodes, second pass
LEAD = 0 # lead node on second pass
#sys.setrecursionlimit(300000)


def load_file(filename):
    """
    Builds graph from specified file location

    input: file location (url or local) (string)
    """
    print "Loading graph..."
    graph = {}
    openers = [urllib2.urlopen, open]
    for func in openers:
        try:
            fileobject = func(filename)
            for line in fileobject:
                nodes = line.split(" ")
                if nodes[0] not in graph:
                    graph[nodes[0]] = [nodes[1]]
                else:
                    graph[nodes[0]].append(nodes[1])
            fileobject.close()
            print "Graph loaded."
            return graph
        except:
            continue
    print "Load failed."


def dfs(graph, node):
    """
    Depth-First Search through each component

    Input:  graph (dict)
            node (int)
    """
    # add node to explored list and notate who its leader is
    EXPLORED.append(node)
    LEADERS[node] = LEAD
    # loop through all of edges coming from node, recurse unvisited
    for edge in graph[node]:
        if edge not in EXPLORED:
            dfs(graph, node)
    # increase time step 1 and set nodes time step to new time
    TIME += 1
    print time
    FTIMES[node] = TIME


def dfs_loop(graph):
    """
    Loop used to calculate strongly connected component

    input: graph (dict)
    """
    max_node = max(graph)
    for node in xrange(max_node, 0, -1):
        if node not in EXPLORED:
            LEAD = node
            dfs(graph, node)


def reverse_graph(graph):
    """
    Loops over directional graph creating an exact copy with each edge reversed

    """
    graph_reversed = {}

    for node in graph:
        for edge in graph[node]:
            if edge in graph_reversed:
                graph_reversed[edge].append(node)
            else:
                graph_reversed[edge] = [node]

    return graph_reversed


def main(graph):
    graph_reversed = reverse_graph(graph)
    dfs_loop(graph_reversed)


def tester():
    graph_one = {
        1: [7],
        2: [5],
        3: [9],
        4: [1],
        5: [8],
        6: [3, 8],
        7: [4, 9],
        8: [2],
        9: [6]
    }
    graph_two = {
        1: [2],
        2: [3, 4],
        3: [1, 8, 9],
        4: [5, 6],
        5: [6],
        6: [7],
        7: [5, 7],
        8: [5, 10, 11],
        9: [8],
        10: [9],
        11: [10]
    }

    print reverse_graph(graph_one)
    print reverse_graph(graph_two)
    print "Graph Reverser test complete."
    main(graph_one)
    print fTimes
    print time
    print "DFS looping complete."
    load_file(SCC_URL)
    print "File load test complete."

tester()
#graph = load_file(filename)
#main(SCC_URL)
