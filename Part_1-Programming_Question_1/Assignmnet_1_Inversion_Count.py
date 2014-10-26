"""
Algorithms: Design and Analysis Part 1
Stanford University

Programming Question 1
Merge Sort - counting inversions
"""

#initialize globals and input files
filename1 = "IntegerTest.txt"
filename2 = "IntegerArray.txt"

def load_file(filename):
	int_file = open(filename, "r")
	ints = int_file.read()
	array_int = map(int, ints.split("\n"))
	return array_int


def inversionCounter(array_int):
	"""
	Takes in list of numbers and computes number of inversions.

	input: list of integers
	output: number of inversions (int)
	"""
	#initialize variables
	sorted_array = []
	array_len = len(array_int)
	inversion_count = 0

	#recursive loop for sorting array
	if array_len < 2:
		return inversion_count, array_int
	else:
		left = inversionCounter(array_int[:(array_len / 2)])
		right = inversionCounter(array_int[(array_len / 2):])

	#merge sorted lists together and count inversions
	inversion_count = inversion_count + left[0] + right[0]
	index_i, index_j = 0, 0
	left_len, right_len = len(left[1]), len(right[1])
	for counter in xrange(array_len):
		if index_i < (left_len) and index_j < (right_len):
			if left[1][index_i] < right[1][index_j]:
				sorted_array.append(left[1][index_i])
				index_i += 1
			else:
				sorted_array.append(right[1][index_j])
				index_j += 1
				inversion_count = inversion_count + (left_len - index_i)
		elif index_i < (left_len):
			sorted_array.append(left[1][index_i])
			index_i += 1
		else:
			sorted_array.append(right[1][index_j])
			index_j += 1

	#return merged arrays and inversion count
	return inversion_count, sorted_array


def test_inversionCounter():
	"""
	Test function for inversionCounter function.

	No input or output, prints to console.
	"""
	#initializing test cases
	arrayTest1 = []
	arrayTest2 = [1]
	arrayTest3 = [2, 1]
	arrayTest4 = [7, 5, 3, 1, 9]
	arrayTest5 = [8, 2, 3, 4, 5, 6, 7, 1]
	arrayTest6 = [1, 3, 5, 2, 4, 6]
	arrayTest7 = [1, 5, 3, 2, 4]
	arrayTest8 = [1, 6, 3, 2, 4, 5]
	arrayTest9 = [9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0]

	#test each and print expected result
	print "Testing inversionCounter function....\n"
	print arrayTest1
	print inversionCounter(arrayTest1)
	print "Expected result: (0, []) \n"
	print arrayTest2
	print inversionCounter(arrayTest2)
	print "Expected result: (0, [1]) \n"
	print arrayTest3
	print inversionCounter(arrayTest3)
	print "Expected result: (1, [1, 2]) \n"
	print arrayTest4
	print inversionCounter(arrayTest4)
	print "Expected result: (6, [1, 3, 5, 7, 9]) \n"
	print arrayTest5
	print inversionCounter(arrayTest5)
	print "Expected result: (13, [1, 2, 3, 4, 5, 6, 7, 8]) \n"
	print arrayTest6
	print inversionCounter(arrayTest6)
	print "Expected result: (3, [1, 2, 3, 4, 5, 6]) \n"
	print arrayTest7
	print inversionCounter(arrayTest7)
	print "Expected result: (4, ...) \n"
	print arrayTest8
	print inversionCounter(arrayTest8)
	print "Expected result: (5, ...) \n"
	print arrayTest9
	print inversionCounter(arrayTest9)
	print "Expected result: (56, ...) \n"

	#end function
	return

#test_inversionCounter()
integer_array = load_file(filename2)
counted_inversions = inversionCounter(integer_array)
print counted_inversions[0]






