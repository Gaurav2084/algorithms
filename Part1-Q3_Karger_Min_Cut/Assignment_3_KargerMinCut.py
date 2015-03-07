"""
Algorithms: Design and Analysis Part 1
Stanford University

Programming Question 3
Graph Minimum Cuts - Karger Min Cut
"""
import random
import copy

# Global variables
FILENAME = "kargerMinCut.txt"


def load_graph(filename):
    """
    Function that loads graph adjacency list

    input: filename (string)
    return: graph (dict)
    """
    # initialize graph variable
    graph = {}

    # load graph from file
    print "Loading graph..."
    with open(filename, 'r') as text_input:
        for line in text_input:
            vertex = [int(x) for x in line.split()]
            graph[vertex[0]] = vertex[1:]

    # return graph
    print "Graph loaded!"
    return graph


def karger_min_cut(graph):
    """
    Function that calculates the min cut using
    Karger Min Randomized Contraction Algorithm

    input: graph adjecency list (dict)
    return: min number of cuts (int)
    """
    # initiate variables
    cuts = 0
    graph_length = len(graph)
    point_u, point_v = None, None  # edge start and end points

    # if only 2 vertices cuts has to be 1
    if graph_length == 2:
        cuts = 1
    # while loop logic that performs contractions
    while graph_length > 2:
        # pick random edge (u, v)
        point_u = random.choice(graph.keys())
        point_v = random.choice(graph[point_u])
        # contract u & v's edges, remove self loops
        vertices = graph[point_u] + graph[point_v]
        new_edges = []
        for point in vertices:
            if (point == point_v) or (point == point_u):
                continue
            new_edges.append(point)
            # inner loop to update new contracted point
            edge_list_length = len(graph[point])
            for index in xrange(edge_list_length):
                if graph[point][index] == point_u:
                    graph[point][index] = point_v
        graph[point_v] = new_edges
        # remove point u and measure graph
        graph.pop(point_u)
        graph_length = len(graph)

    # return number of cuts after contraction
    cuts = len(graph[random.choice(graph.keys())])
    return cuts


def min_cut_trials(graph, num_trials):
    """
    Trial simulator for counting min cuts.

    input: graph (dict)
            number of trials (int)
    return: minimum # of cuts (int)
    """
    # initialize min so far
    min_cut, current_cut = None, None

    # trial logic
    print "Trial",
    for trial in xrange(num_trials):
        print trial, "...",
        graph_copy = copy.deepcopy(graph)
        current_cut = karger_min_cut(graph_copy)
        if (current_cut < min_cut) or (min_cut is None):
            min_cut = current_cut

    # return the lowest found
    print "complete"
    return min_cut


def tester():
    """
    Tester Function
    """
    # test graphs
    graph_1 = {
        1: [2, 3, 4],
        2: [1, 3, 4],
        3: [1, 2, 5],
        4: [1, 2, 5],
        5: [3, 4]
    }

    # test function calls
    print "Test 1"
    test1 = min_cut_trials(graph_1, 20)
    print "Result: ", test1, "Correct Answer: 2"
    return

# run tester first
#tester()

# load file and find result
graph = load_graph(FILENAME)
result = min_cut_trials(graph, 20)
print "Result:", result
