# Algorithms: Design and Analysis Part 1
# Stanford University

# Programming Question 6 - Part 1
# Count number of 2 sum variations where x + y = t
# t is any integer in interval [-10000, 10000]
# Hash table utilization problem

import urllib2

# constants
SUM_URL = "https://d396qusza40orc.cloudfront.net/" + \
          "algo1%2Fprogramming_prob%2F2sum.txt"
TARGET_SUM = 10000


def stream_file(filename):
    """
    Method for reading in a large file and generating one line at a time
    :param filename: file location (string)
    :return: yields one line from file at a time (int)
    """
    yield int


def main(target_sum, filename):
    """
    Main control for program.  Takes each line provided by stream_file
    and checks if exists in hash, if not calculates number of variants
    that meat target_sum provide.
    :param target_sum: absolute value max sum (int)
    :param filename: location of file to read (string)
    :return: count: total number (int)
    """
    numbers = {}  # hash to be used to track
    count = 0  # total variations for x + y = t

    # grab each number from filestream as read
    for current_num in stream_file(filename):

        # check if already seen current number
        if current_num in numbers:
            continue

        # insert number into hash, search for 2-sum variants
        numbers[current_num] = []
        for number in numbers:
            sum = abs(number + current_num)
            if sum <= target_sum:
                numbers[number].append(current_num)
                numbers[current_num].append(number)
                count += 1

    # after all numbers read from file return count
    return count
