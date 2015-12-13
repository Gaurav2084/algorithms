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


def open_file(filename):
    """
    Reads in file from disk and inputs into an array
    :param filename: file location (string)
    :return: num_array: list of numbers
    """
    num_array = list()

    # open file and read each line into array
    print "Loading file..."
    file_object = urllib2.urlopen(filename)
    for line in file_object:
        num_array.append(int(line))
    file_object.close()
    print "File loaded."
    return num_array


def main(target_sum, filename):
    """
    Main control for program.  Takes each line provided by stream_file
    and checks if exists in hash, if not calculates number of variants
    that meat target_sum provide.
    :param target_sum: positive value max sum (int)
    :param filename: location of file to read (string)
    :return: count: total number (int)
    """
    numbers = dict()
    processed = 0
    sums = dict()

    # get num array from file then insert into hash, de-duping
    num_array = open_file(filename)
    print "Loading numbers into hash..."
    for current_num in num_array:
        numbers[current_num] = True

    # Iterate through hash and search for each numbers counter range
    print "Searching for 2-Sum variants..."
    for num in numbers:
        processed += 1
        for range_num in xrange(target_sum * -1, target_sum + 1):
            counter_num = range_num - num

            # if number exists hash, solution is possible
            if num == counter_num or counter_num not in numbers or \
               range_num in sums:
                continue
            pair = tuple(sorted([counter_num, num]))
            sums[range_num] = pair

        if processed % 20000 == 0:
            print "Processed 20,000 more, at " + str(processed)
            print "Current total is " + str(len(sums))

    # after all numbers read from file return count
    return len(sums)


# Process main program logic with both given constants
print "Answer is: " + str(main(TARGET_SUM, SUM_URL))
