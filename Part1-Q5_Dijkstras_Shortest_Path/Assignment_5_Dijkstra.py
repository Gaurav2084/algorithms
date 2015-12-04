# Algorithms: Design and Analysis Part 1
# Stanford University

# Programming Question 5
# Compute shortest path from vertex 1 to selected vertices:
# 7,37,59,82,99,115,133,165,188,197
# Dijkstra Shortest Path Algorithm in Adjacency List

import urllib2
import re

# constants
SP_URL = ("http://spark-public.s3.amazonaws.com"
          "/algo1/programming_prob/dijkstraData.txt")
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
    # loop through both types of file openers and try to open file
    for openFunction in openers:
        try:
            fileObject = openFunction(filename)
            # process each line converting first node to key and rest to list
            for line in fileObject:
                nodes = line.split("\t")
                keyNode = convert_integer(nodes[0])
                if keyNode not in graph:
                    # loop through each node converting to int
                    node_list = []
                    for node in nodes[1:]:
                        node = convert_integer(node)
                        if node:
                            node_list.append(int(node))
                    # attach list of nodes back to key node
                    graph[keyNode] = node_list
            fileObject.close()

            print "Graph loaded."
            return graph
        # if IOError ignore, any other error needs to be printed
        except IOError:
            pass
        except Exception as e:
            print e
            pass
    print "Load failed."


def convert_integer(string_int):
    """
    Takes a string that contains integers and removes all extra characters
    returning only the integers

    input: string to convert (string)
    output: new integer (int)
    """
    new_num = ""
    # replace extra characters with nothing then convert to int
    clean_string = re.sub('[,\n\r]', '', string_int)
    if len(clean_string) > 0:
        new_num = int(clean_string)
    return new_num


def dijkstra(graph, start_node, end_nodes):
    """
    Main construct for dijkstra's algorithm.  Loops through using BFS
    calculating weights until shortest path is found.  Assumes no self loops
    and no negative weights.

    input:  graph (dict of dicts)
            start_node (string or int of node in graph)
            end_nodes (list of string or int of nodes in graph)
    output: distances (list of ints)
    """
    # initialize array for shortest path distances
    shortest_paths = []
    max_distance = 1000000

    # loop through end_nodes and compute shortest paths
    for end_node in end_nodes:
        nodes_touched = []
        node_queue = [{start_node: start_node}]
        distances = {(start_node, start_node): 0}
        current_node = start_node

        while node_queue:
            for to_visit in graph[current_node]:



        # after search complete append the distance found
        shortest_paths.append(distances[(start_node, end_node)])

    return shortest_paths


def main():
    """
    Main construct for assignment.
    """
    # first run dijsktra on a test graph with known answer
    test_graph = {}
    test_graph["s"] = {"v": 1, "w": 4}
    test_graph["v"] = {"w": 2, "t:": 6}
    test_graph["w"] = {"t": 3}
    test_graph["t"] = {}
    print "Expect result: [6]"
    # print "Actual result: " + dijkstra_main(test_graph, "s", ["t"])

    # end nodes that need to find shortest paths for
    end_nodes = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    # graph = load_file(SP_URL)
    print "Expect result: [2599, 2610, 2947, 2052, 2367, " +
    "2399, 2029, 2505, 3068]"
    # print "Actual result: " + dijkstra_main(graph, 1, end_nodes)
