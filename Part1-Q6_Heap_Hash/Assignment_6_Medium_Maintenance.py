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
    total_nums = 0
    # create lesser half heap and track stats
    low_heap, max_low, total_low = list, 0, 0
    # create greater half heap and track stats
    high_heap, min_high, total_high = list, 0, 0

    # loop through numbers from file
    for number in stream_file(filename):
        total_nums += 1

        if number <= max_low:
            heapq.heappush(low_heap, (-1 * number))
            total_low += 1
            max_low = -1 * heapq.heappop(low_heap)
        else:
            heapq.heappush(high_heap, number)
            total_high += 1
            min_high = heapq.heappop(high_heap)

        # balance heaps if too many numbers in either one
        if (total_low - total_high) > 1:
            heapq.heappush(high_heap, max_low)
            max_low = -1 * heapq.heappop(low_heap)
        elif (total_high - total_low) > 1:
            heapq.heappush(low_heap, min_high)
            min_high = heapq.heappop(high_heap)

        # determine if on even or median and calculate
        if total_nums % 2 == 0:
            median_sums += max_low
        else:
            median_sums += min_high

    # return sum of all medians modulo total numbers
    return median_sums % total_nums


# print to console result of the algorithm on given file
print "Answer is: " + str(main(MEDIAN_URL))
