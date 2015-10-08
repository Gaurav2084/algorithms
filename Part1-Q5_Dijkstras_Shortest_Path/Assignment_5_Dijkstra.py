# Algorithms: Design and Analysis Part 1
# Stanford University

# Programming Question 5
# Compute shortest path from vertex 1 to selected vertices:
# 7,37,59,82,99,115,133,165,188,197
# Dijkstra Shortest Path Algorithm in Adjacency List

import urllib2

# globals
SP_URL = "http://spark-public.s3.amazonaws.com/algo1/programming_prob/dijkstraData.txt"
SP_LOCAL = "dijkstraData.txt"

def load_file(filename):
    """
    Builds graph from specified file location

    input: file location (url or local) (string)
    output: direction graph (dict)
    """
    print "Loading graph..."
    graph = {}
    openers = [urllib2.urlopen, open]
    for openFunction in openers:
        try:
            fileObject = openFunction(filename)
            for line in fileObject:
                print line
                nodes = line.split("\t")
                keyNode = int(nodes[0])
                if keyNode not in graph:
                    graph[keyNode] = nodes[1:]  # TODO convert to ints and remove extra chars
                print graph
                return # TODO remove when ready to load entire graph
            fileObject.close()
            print "Graph loaded."
            return graph
        except:
            continue
    print "Load failed."

load_file(SP_LOCAL)
