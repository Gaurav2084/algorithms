# Algorithms: Design and Analysis Part 1
# Stanford University

# Programming Question 4
# Strongly Connected Components (Compute Largest 5)
# Depth-First Search SCC for directed graph
# Kosaraju's Two-Pass Algorithm

import urllib2

# globals
SCC_URL = "http://spark-public.s3.amazonaws.com/algo1/programming_prob/SCC.txt"
SCC_LOCAL = "/Users/Hyperion/Desktop/SCC.txt"


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
            return
        except:
            continue
    print "Load failed."


def dfs(graph, node):
    """
    Depth-First Search through each component

    Input:  graph (dict)
            node (int)
    """
    global time
    # add node to explored list and notate who its leader is
    explored.append(node)
    leaders[node] = lead
    # loop through all of edges coming from node, recurse unvisited
    for edge in graph[node]:
        if edge not in explored:
            dfs(graph, node)
    # increase time step 1 and set nodes time step to new time
    time += 1
    fTimes[node] = time


def dfs_loop(graph):
    """
    Loop used to calculate strongly connected component

    input: graph (dict)
    """
    max_node = max(graph)
    for node in xrange(max_node, -1, -1):
        if node not in explored:
            lead = node
            dfs(graph, node)


def main(filename):
    global time  # finishing times for nodes, first pass
    global lead  # leaders for nodes, second pass
    global explored = []  # explored nodes
    global leaders = {}
    global fTimes = {}  # associated leaders and finishing times
    load_file(filename)


def tester():
    graph_one = {
        1: [7],
        2: [5],
        3: [9],
        4: [1],
        5: [8],
        6: [3],
        7: [9],
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
    pass

tester()
#main(SCC_URL)
