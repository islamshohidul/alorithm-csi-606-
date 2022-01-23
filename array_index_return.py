###Author Md Shohidul
# From a given array return sum of 2 values index that equal target value
#
###
#
#
###
#
#
###
#
#
###
#
#
import math

def naiveApproach(array, target):
	n = len(array)
	for i in range(n):
		for j in range(n):
			if array[i] + array[j] == 50:
				return i,j
		

array = [10,20,10,40]

#print (naiveApproach(array,50));
	

#slide better appraoch using binary search

def  binarySearchApproach(array,target):
	
	sorted_array = sorted(array)
	n = len(array)
	
	for i in range (n):
		x= array[i]
		
		found = binarySearch(sorted_array, target-sorted_array[i])
		
		if found:
			return  i;
			
def binarySearch(array, target):

	l = 0;
	r = len(array)-1
	
	while(l<r):
		x = l+r/2
		mid = math.ceil(x)
		
		
		if array[mid] > target:
			r = mid-1;
		
		elif array[mid] < target:
			l = mid+1;
		
		else:
			return True
#print (binarySearchApproach(array,50));				

def twoPointersApproach(array,target):
	sortedArray = sorted(array);
	left = 0;
	right = len(array) -1;
	
	while (left < right):
		x = sortedArray[left];
		y = sortedArray[right];
		sum = x+y
		
		if sum == target :
			found  = True
			
		if sum < target:
			left += left;
			
		if sum > target:
			right -=right;
			
		if found:
			return left , right	
#print (twoPointersApproach(array,50));


def bestApproach(array, target):
	
	dictA = {};
	size = len(array);
	
	for i in range (size):
		if (target-array[i]) in dictA:
		
			return dictA[target-array[i]], i ;
		
		dictA[array[i]] = i
	



print (bestApproach(array,50));















