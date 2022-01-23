

def sliding_window_algorithm(array,x):

	currentSum = sum(array[:x]);
	maxSum = currentSum;
	n = len(array)
	for i in range(n-x):
		currentSum = currentSum - array[i] + array[x+i]
		maxSum = max(currentSum, maxSum);
	return maxSum;	 
	


array = [ 5, 7, 1, 4, 3, 6, 2, 9, 2 ]

print (sliding_window_algorithm(array,5))
