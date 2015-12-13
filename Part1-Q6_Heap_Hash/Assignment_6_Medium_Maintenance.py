# Algorithms: Design and Analysis Part 1
# Stanford University

# Programming Question 6 - Part 2
# Find median for set of numbers as they are given 1 by 1
# Median Maintenance utilizing heaps

import urllib2
import heapq


# constants
MEDIAN_URL = "http://spark-public.s3.amazonaws.com/" + \
             "algo1/programming_prob/Median.txt"


def stream_file(filename):
    """
    Generates integers from a give file location URL.
    :param filename: file location (string)
    :return: yeild 1 integer from file as called
    """
    file_object = urllib2.urlopen(filename)
    for line in file_object:
        yield int(line)
    file_object.close()


def main(filename):
    """
    Main program logic for median maintenance algorithm.
    :param filename: file location of integers (string)
    :return: sum of ints modulo number of ints (int)
    """
    median_sums = 0
    low_heap, high_heap = [], []
    max_low = 0

    # loop through numbers from file
    for number in stream_file(filename):
        # determine which heap the next number goes into
        if number <= max_low:
            heapq.heappush(low_heap, (-1 * number))
        else:
            heapq.heappush(high_heap, number)

        # keep heaps even or low_heap with one additional
        if (len(low_heap) - len(high_heap)) > 1:
            max_low = -1 * heapq.heappop(low_heap)
            heapq.heappush(high_heap, max_low)
            max_low = -1 * low_heap[0]
        elif (len(high_heap) - len(low_heap)) >= 1:
            max_low = heapq.heappop(high_heap)
            heapq.heappush(low_heap, -1 * max_low)

        # add highest low number to median every time
        median_sums += max_low

    # return sum of all medians modulo total numbers
    return median_sums % (len(low_heap) + len(high_heap))


# print to console result of the algorithm on given file
print "Answer is: " + str(main(MEDIAN_URL))
