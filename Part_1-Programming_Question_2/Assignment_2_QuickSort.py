"""
Algorithms: Design and Analysis Part 1
Stanford University

Programming Question 2
QuickSort - counting comparisons
"""
import pdb

#initialize global variables
FILENAME = "QuickSort.txt"


def load_file(filename):
    """
    Load text file of integers.

    Input: filename (string)
    """
    with open(filename, "r") as int_file:
        ints = int_file.read()
        array_int = map(int, ints.split("\n"))
    return array_int


def partition(array_ints, left, right):
    """
    Takes starting element, ending element and partitions input array into
    two sets of elements either less than or greater than.

    input: array of integers (list)
        left most index to begin with (integer)
        right most index to stop at (integer)
    return: pivot location (int)
    """
    #variables initialized for partitioning
    pivot_element = array_ints[left]
    index_i = left + 1

    #loop through array doing comparisons with partition element
    for index_j in xrange(index_i, right + 1):
        if array_ints[index_j] < pivot_element:
            array_ints[index_j], array_ints[index_i] = array_ints[index_i], array_ints[index_j]
            index_i += 1

    #finally swap pivot element and index i element
    array_ints[index_i - 1], array_ints[left] = array_ints[left], array_ints[index_i - 1]
    return index_i - 1


def create_pivot(array_ints, left, right, pivot_method):
    """
    Takes in pivot method and sorts appropiate pivot to first position in array.
    If no method given it assumes first element as pivot.

    input: method (string), array of ints, left (int), right (int)
    output: None
    """
    #initiate pivot_index
    pivot_index = left
    middle, median = None, None
    array_length = len(array_ints[left:right + 1])

    #swaps last element with first element for pivot
    if pivot_method in ("last", "end"):
        pivot_index = right
    #finds median of first, last and middle elements and swaps to first position
    elif pivot_method in ("median", "middle"):
        if array_length > 2:
            middle =  left + (int(round(array_length / 2.0)) - 1)
            median = sorted([array_ints[left], array_ints[middle], array_ints[right]])[1]
        elif array_length == 2:
            median = min([array_ints[left], array_ints[right]])
        pivot_index = array_ints.index(median)

    #swap pivot_index chosen with current first element
    array_ints[left], array_ints[pivot_index] = array_ints[pivot_index], array_ints[left]
    return


def quicksort_count(array_ints, left=0, right=None, pivot_method=""):
    """
    Takes input array, left starting position, right ending position, and
    pivot method for choosing pivot. Sorts elements using QuickSort algorithm
    and counts number of comparisons.

    input: array of integers, left (int), right (int), pivot_method (string)
    """
    #initialize count and pivot elements variable
    count, count_left, count_right = 0, 0, 0
    pivot_index = None
    if right is None:
        right = len(array_ints) - 1

    #process quicksort logic if array longer than 1
    if len(array_ints[left:right + 1]) > 1:
        create_pivot(array_ints, left, right, pivot_method)
        count = len(array_ints[left:right])
        pivot_index = partition(array_ints, left, right)
        if pivot_index > left:
            count_left = quicksort_count(array_ints, left, pivot_index - 1, pivot_method)
        if right > pivot_index:
            count_right = quicksort_count(array_ints, pivot_index + 1, right, pivot_method)

    #add count from inital partition and recursive partitions
    return count + count_left + count_right


def test_quicksort():
    """
    Test function for building algorithm and not loading entire array set yet.
    Not complete test of all conditions.
    """
    #test arrays
    array_one = [1]
    array_two = [2, 1]
    array_three = [3, 2, 1]
    array_four = [5, 1, 2, 4, 3]
    array_five = [1, 2, 3, 4, 5, 6]
    array_six = [6, 2, 5, 4, 1, 3]

    #print test functions
    print "Testing QuickSort function \n"
    print quicksort_count(array_one), 
    print array_one
    print "0 [1] - answer\n"
    print quicksort_count(array_two),
    print array_two
    print "1 [1, 2] - answer\n"
    print quicksort_count(array_three),
    print array_three
    print "3 [1, 2, 3] - answer\n"
    print quicksort_count(array_four),
    print array_four
    print "8 [1, 2, 3, 4, 5] - answer\n"
    print quicksort_count(array_five),
    print array_five
    print "15 [1, 2, 3, 4, 5, 6] - answer\n"
    print quicksort_count(array_six),
    print array_six
    print "11 [1, 2, 3, 4, 5, 6] - answer\n"


def count_comparisons():
    """
    Function to run main comparison.
    """
    initial_array = load_file(FILENAME)
    array_to_count = initial_array[:]
    comparisons_pivot_first = quicksort_count(array_to_count)
    print comparisons_pivot_first
    print "Correct answer = 162085\n"
    #print array_to_count
    array_to_count = initial_array[:]
    comparisons_pivot_last = quicksort_count(array_to_count, pivot_method = "end")
    print comparisons_pivot_last
    print "Correct answer = 164123\n"
    #print array_to_count
    array_to_count = initial_array[:]
    comparisons_pivot_median = quicksort_count(array_to_count, pivot_method = "median")
    print comparisons_pivot_median
    print "Correct answer = 138382\n"
    #print array_to_count

#test_quicksort()
count_comparisons()
