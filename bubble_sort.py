"""
Author: Md Shohidul Islam

The idea behind the bubble sort is comparing the 2 adjacent value till all the value reach it's exact position.
Algorithm:
bubbleSort(array A)
	size = A.length
	sum = 0
	for i = 1 to size-1
		swapped = false 
		for j = 1 to size-1
			if A[j] > A[j+1]
				swap(A[j],A[j+1])
				swapped = true
	if(swapped == false)
		break			
			
"""

# CODE BEGIN FROM HERE

def bubbleSort(array):

	size = len(array)
		
	for i in range(size-1):
		swapped = False
		for j in range (size-i-1):
			if array[j] > array[j+1]:
				temp = array[j]
				array[j] = array[j+1]
				array[j+1] = temp
				swapped = True
		if swapped == False:
			break
	
	return array	

array =  [3,2,1]	



bubbleSort(array)				
		
	

