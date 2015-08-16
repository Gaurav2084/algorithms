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
Time = 0 # finishing times for nodes, first pass
FTimes = {} # associated leaders and finishing times
Explored = [] # explored nodes
Leaders = {} # leaders for nodes, second pass
Lead = 1 # lead node on second pass
#sys.setrecursionlimit(300000)


def load_file(filename):
    """
    Builds graph from specified file location

    input: file location (url or local) (string)
    output: direction graph (dict)
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

    input:  graph (dict)
            node (int)
    """
    global Time
    # add node to explored list and notate who its leader is
    Explored.append(node)
    Leaders[node] = Lead
    # loop through all of edges coming from node, recurse unvisited
    for edge in graph[node]:
        if edge not in Explored:
            dfs(graph, edge)
    # increase time step 1 and set nodes time step to new time
    Time += 1
    FTimes[node] = Time


def dfs_loop(graph):
    """
    Loop used to calculate strongly connected component

    input: graph (dict)
    """
    global Lead
    # find last node to work backwards through graph
    max_node = max(graph)
    # loop through graph running dfs() if node hasn't been visited
    for node in xrange(max_node, 0, -1):
        if node not in Explored:
            Lead = node
            dfs(graph, node)


def reverse_graph(graph):
    """
    Loops over directional graph creating an exact copy with each edge reversed

    input: graph (dict)
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
    """
    Logic for using DFS to compute strongly connected component

    input: direction graph (dict)
    output largest 5 strongly connected comp. (tuple of ints)
    """
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
    print FTimes
    print Leaders
    print "DFS looping complete."
    # load_file(SCC_URL)
    # print "File load test complete."

tester()
#problem_graph = load_file(SCC_URL)
#main(problem_graph)
