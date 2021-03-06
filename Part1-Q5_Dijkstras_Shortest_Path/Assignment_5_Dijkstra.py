# Algorithms: Design and Analysis Part 1
# Stanford University

# Programming Question 5
# Compute shortest path from vertex 1 to selected vertices:
# 7,37,59,82,99,115,133,165,188,197
# Dijkstra Shortest Path Algorithm in Adjacency List

import urllib2

# constants
SP_URL = ("http://spark-public.s3.amazonaws.com"
          "/algo1/programming_prob/dijkstraData.txt")
SP_LOCAL = "dijkstraData.txt"
MAX_DISTANCE = 1000000


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
                keyNode = int(nodes[0]) # first node is key
                weighted_edges = {}
                for node in nodes[1:-1]: # skip first and leave off last
                    edge, weight = node.split(",")
                    weighted_edges[int(edge)] = int(weight)
                # attach list of edges with weights back to key node
                graph[keyNode] = weighted_edges
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


def dijkstra_loop(graph, start_node, end_node):
    """
    Loop for computing shortest path between two nodes.

    input:  graph
            start_node
            end_node
    return: shortest_path distance (int)
    """
    # initialize visited nodes and start queue with initial node as first
    # edge, giving itself a distance of zero
    visited = []
    edge_queue = set([(start_node, start_node)])
    distances = {(start_node, start_node): 0}
    final_edge = (start_node, end_node)

    while edge_queue:
        # extract path with lowest edge weights thus far
        shortest_path = None
        for edge in edge_queue:
            if not shortest_path or distances[edge] < shortest_path:
                shortest_path = distances[edge]
                current_edge = edge
        edge_queue.remove(current_edge)

        # assign nodes to calculate the next round of distances
        current_node = current_edge[1]
        visited.append(current_node)

        # if current node is end search path is complete
        if current_node == end_node:
            break

        # loop through next set of nodes touching the end of the current
        # edge and calculate their distances in reference to start node
        for to_visit in graph[current_node]:
            edge = (start_node, to_visit)
            add_dist = distances[current_edge] + graph[current_node][to_visit]
            # only queue up edges to nodes not visited
            if to_visit not in visited:
                edge_queue.add(edge)
            # record distances if don't exist or smaller weight
            if edge not in distances or distances[edge] > add_dist:
                distances[edge] = add_dist

    # finally if the two nodes don't meet assign the max distance
    if final_edge not in distances:
        distances[final_edge] = MAX_DISTANCE
    return distances[final_edge]


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

    # loop through end_nodes and compute shortest paths
    for end_node in end_nodes:
        path = dijkstra_loop(graph, start_node, end_node)
        shortest_paths.append(path)

    return shortest_paths


def main():
    """
    Main construct for assignment.
    """
    # first run dijsktra on a test graph with known answer
    test_graph = {}
    test_graph["s"] = {"v": 1, "w": 4}
    test_graph["v"] = {"w": 2, "t": 6, "s": 1}
    test_graph["w"] = {"t": 3, "s": 4, "v": 2}
    test_graph["t"] = {"w": 3, "v": 6}
    print "Actual result: " + str(dijkstra(test_graph, "s", ["t"]))

    # end nodes that need to find shortest paths for
    end_nodes = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    graph = load_file(SP_URL)
    print "Actual result: " + str(dijkstra(graph, 1, end_nodes))

main()
