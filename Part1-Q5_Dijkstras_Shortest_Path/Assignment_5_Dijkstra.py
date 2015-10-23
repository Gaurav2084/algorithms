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


def dijkstra_loop(start_node):
    """
    Loop for dijkstra

    Input: start node (int)
    """
    vertices_touched = [start_node]

    return


def dijkstra_main(datalink):
    """
    Main program for dijkstra algorithm.
    """
    graph = load_file(datalink)


    return


#load_file(SP_URL)
