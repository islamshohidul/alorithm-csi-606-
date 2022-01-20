"""
Author: Md Shohidul Islam
The total sum of an array value will be calculated with this code.
Algorithm:

sum(array A)
	size = A.length
	sum = 0
	for i = 1 to size
		sum = sum + A[i]
			

"""

# CODE BEGIN FROM HERE

def sum (array):
	
	n = len(array);
	sum = 0;
	
	for i in range(n):
		sum = sum + array[i];
	
	print (sum);

array = [23,34,4,34,34,3,56,7,7687,76];

sum(array);

# END OF THE CODE		
