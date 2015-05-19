# Algorithms: Design and Analysis Part 1
# Stanford University

# Programming Question 4
# Strongly Connected Components (Compute Largest 5)
# Depth-First Search SCC for directed graph
# Kosaraju's Two-Pass Algorithm

import urllib2

# global name of file location
SCC_FILE = "http://spark-public.s3.amazonaws.com/algo1/programming_prob/SCC.txt"
LOCAL = ""


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
            with func(filename) as fileobject:
                for line in fileobject:
                    nodes = line.split(" ")

            print "Load complete."
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



def main():
    pass


def tester():
    pass
