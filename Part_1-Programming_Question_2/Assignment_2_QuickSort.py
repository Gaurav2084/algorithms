"""
Algorithms: Design and Analysis Part 1
Stanford University

Programming Question 2
QuickSort - counting comparisons
"""

#initialize global variables
FILENAME = "QuickSort.txt"


def load_file(filename):
    int_file = open(filename, "r")
    ints = int_file.read()
    array_int = map(int, ints.split("\n"))
    return array_int

	
def load_file2(filename):
    with open(filename, "r") as int_file:
        ints = int_file.read()
        array_int = map(int, ints.split("\n"))
        #array_int = ints.read().splitlines()
    return array_int


def partition(array, left, right):
    """
    Takes starting element and partitions input array into 
    two sets of elements either less than or greater than.

    input: array of integers (list)
	    left most index to begin with (integer)
        right most index to stop at (integer)
    return: None
    """
    #variables initialized for partitioning
    pivot_element = array[left]
    index_i = left + 1

    #loop through array doing comparisons with partition element
    for index_j in xrange(index_i, right + 1):
        if array[index_j] < pivot_element:
            array[index_j], array[index_i]  = array[index_i], array[index_j]
            index_i += 1

    #finally swap pivot element and index i element
    array[index_i - 1], array[left] = array[left], array[index_i - 1]
    return index_i


def create_pivot(array, pivot_method):
    """
    Takes in pivot method and sorts appropiate pivot to first position in array. 
    If no method given it assumes first element as pivot.

    input: method (string), array of ints
    output: pivot location (integer)
    """
    if pivot_method in ("last", "end"):
        pivot_index = len(array) - 1
        array[0], array[pivot_index] = array[pivot_index], array[0]
    return 


def quicksort_count(array, left=0, right=None, pivot_method=""):
    """
    Takes input array and sorts elements using QuickSort algorithm.

    input: array of integers
    """
    #initialize count and pivot elements variable
    count, count_left, count_right = 0, 0, 0
    pivot_index = None
    if right is None:
        right = len(array) - 1
	    
    #process quicksort logic if array longer than 1
    if ((right + 1) - left) > 1:
        create_pivot(array, pivot_method)
        count = (right - left)
        pivot_index = partition(array, left, right)
        if ((pivot_index - 1) - left) > 1:
            count_left = quicksort_count(array, left, pivot_index - 1, pivot_method)
        if (right - pivot_index) > 1:
            count_right = quicksort_count(array, pivot_index, right, pivot_method)

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
    print "7 [1, 2, 3, 4, 5] - answer\n"
    print quicksort_count(array_five),
    print array_five
    print "9 [1, 2, 3, 4, 5, 6] - answer\n"
    print quicksort_count(array_six),
    print array_six
    print "9 [1, 2, 3, 4, 5, 6] - answer\n"


def count_comparisons():
    """
    Function to run main comparison.
    """
    initial_array = load_file2(FILENAME)
    array_to_count = initial_array[:]
    comparisons_pivot_first = quicksort_count(array_to_count)
    print comparisons_pivot_first
    print "Correct answer = 162085\n"
    #print array_to_count
#    array_to_count = initial_array[:]
#    comparisons_pivot_last = quicksort_count(array_to_count, pivot_method = "end")
#    print comparisons_pivot_last
#    print "Correct answer = 164123\n"
#    print array_to_count
#    array_to_count = initial_array[:]
#    comparisons_pivot_median = quicksort_count(array_to_count, pivot_method = "median")
#    print comparisons_pivot_median
#    print array_to_count

test_quicksort()
#count_comparisons()


