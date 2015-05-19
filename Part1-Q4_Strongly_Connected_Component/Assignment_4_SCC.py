# Algorithms: Design and Analysis Part 1
# Stanford University

# Programming Question 4
# Strongly Connected Components (Compute Largest 5)
# Depth-First Search SCC for directed graph
# Kosaraju's Two-Pass Algorithm

import urllib2

# global name of file location
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


def dfs_loop(graph):
    """
    Loop used to calculate strongly connected component

    input: graph (dict)
    """
    time = 0  # finishing times for nodes, first pass
    lead = None  # leaders for nodes, second pass
    explored = []
    max_node = max(graph)
    for node in xrange(max_node, -1, -1):
        if node not in explored:
            lead = node
            dfs(graph, node, time, lead)


def dfs(graph, explored, node, times, lead):
    """
    Depth-First Search through each component

    Input:  graph (dict)
            node (int)
            times (int)
            lead (int)
    """
    explored.append(node)


def main(filename):
    load_file(filename)


def tester():

    pass

tester()
#main(SCC_URL)
