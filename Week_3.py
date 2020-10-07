		#############################
		#####	NPTEL - COURSE	#####
		#############################

#########################################################################
#####	Programming, Data Structures and Algorithms Using Python    #####
#########################################################################

############################	WEEK 3	#################################

#########################################################################
##################	Lecture 1: More About Range()	#################
#########################################################################

# NOTES

#	range(i,j) -> i, i+1, ...j-1
#	range(j) -> 0, 1, 2,...j-1
#	range(i,j,k) -> increments by i, i+k, ....i+nk Where i + nk < j
#	if k is negative the range will counnt down i > j

#	list(range(0,5)) == [0,1,2,3,4] #Type Conversion

#########################################################################
##################	Lecture 2: Manipulating Lists	#################
#########################################################################

#	list1 = [1,3,5,6]
#	list2 = list1
#	list1 = list1[0:2] + [7] + list1[3:]
#	list1 is now [1,3,7,6]
#	But list2 remains as [1,3,5,6] since concatenation a list creates a new list.

#	Extending a List
#	l = l +[22]
#	use append to add a value to a list without creating a new list.
#	list1.append(v)
#	list1.extend(list2)
#	list.remove(x) # Removes the first occurance of the list.

#	Example
list1 = list(range(20))
list1.append(21)
list1.extend([22,23])
list2 = list1 + list1
list2.remove(5)
#print(list1)
#print(list2)

#	list1 = [1,3,5,6]
#	list2 = list1
#	list[2:] = [7,8]
#	list1 will be [1,3,7,8]
#	list[2:] = [7,8,9]
#	list1 will be [1,3,7,8,9] #List length will be 5
#	list1[0:2] = [7] #Shrinking of Lists.
#	list1 = [7,9,10,11]

#	Safely remove all occurances of x in l
#	while x in l:
#		l.remove(X)

#	Other Function

#	l.reverse() - reverse the list
#	l.sort() - Sort list in ascending order
#	l.index(x) - Find the index of the leftmost element in a list
#	l.rindex(x) - Find the index of the rightmost element of th list.

#########################################################################
##################	Lecture 3: Breaking out of Loop	#################
#########################################################################

def findpose(l,v):
	#	Return first position of v in l
	#	Return -1 if v not in l
	pos = -1
	for i in range(len(l)):
		if l[i] == v:
			pos = i
			break #Break exits the loop
	else:
		pos = -1 #If var does exit the loop normally without break then this gets executed.
	return(pos)


#########################################################################
###########	Lecture 4: Arrays vs Lists - Binary Search	#########
#########################################################################

#	Arrays - Single Block of memory. elements of uniform type.
#	Indexing is Fast.
#	Inserting and Contraction is complex.
#	seq[i] - Array sequence
#	Unsorted and Sorted Sequence.

#	Binary Search Algorithm for Sorted Sequence

def bsearch(seq, v, l, r):
	#search for v in seq[l:r], seq is sorted
	if(r-l == 0):
		return(False)
	mid = (l+r)//2
	if(v == seq[mid]):
		return(True)
	if(v < seq[mid]):
		return (bseacrh(seq, v, l, mid))
	else:
		return (bsearch(seq, v, mid+1, r))

#	T(n): Time to search the list
#	T(0) = 1
#	T(n) = 1 + T(n/2)

#	Unwind the recurrence
#	T(n)	= 1 + T(n/2)
#			= 1 + 1 + T(n/2^2)... T(n/2^k)
#			= 1 + 1 + 1 + T(n/2^logn) = O(log(n))

#########################################################################
######################	Lecture 5: Efficieny	#########################
#########################################################################

#	Best Case and Worst Case Behaviour.
#	Why considering Worst Case scenario is suggested!

#	T(n) proportional to logn, n, nlogn, n^2,...2^n, n!
#	Each is represented by O ( Big o )

#	Details about the Time Taken by python to evaluate functions
#	Generally	Sorted array - O(logn
#				Unsorted array - O(n)
#	Use time funnction to find the time taken.

#########################################################################
######################	Lecture 6: Selection Sort	#################
#########################################################################

#	Select the next element in sorted order place it in the final sorted list.

def SelectionSort(l):
	#Scan slices 
	for start in range(len(l)):
		for i in range(start,len(l)):
			minpos = start
			if l[i] <l[minpos]:
				minpos = i
			(l[start],l[minpos]) = (l[minpos],l[start])
	return(l)
l = list(range(10,0,-1))
#print(SelectionSort(l))

#	T(n) = O(n^2)

#########################################################################
######################	Lecture 7: Insertion Sort	#################
#########################################################################

def InsertionSort(seq):
	for sliceEnd in range(len(seq)):
		pos = sliceEnd
		while pos > 0 and seq[pos] < seq[pos-1]:
			(seq[pos],seq[pos-1]) = (seq[pos-1],seq[pos])
			pos = pos-1
	return(seq)
#seq = list(range(20,0, -1))
seq = [2,5,4,1]
#print(InsertionSort(seq))

#	T(n) = O(n^2)
#	Fasst for already Sorted List.

#########################################################################
######################	Lecture 8: Recursion	#########################
#########################################################################

#	Inductive Definitions ( Fibonacci Series )

#	m * n = m + (m * (n-1))
#	m * (n+1) = m + (m*n)

#	Inductive series always leads to recursive programs

def factorial(n):
	if n == 0:
		return(1)
	else:
		return(n * factorial(n-1))
#print(factorial(6))

#	Lists can be decomposed as a recursive series

def sumlist(l):
	if l == []:
		return(0)
	else:
		return(l[0] + sumlist(l[1:]))

#	Recursive Insertion Sort

def RInsertionSort(seq):
	isort(seq,len(seq))
	return(seq)

def isort(seq, k):
	if k>1:
		isort(seq, k-1)
		insert(seq,k-1)
	return(seq,k)

def insert(seq, k):
	pos = k
	while pos > 0 and seq[pos] < seq[pos-1]:
		(seq[pos],seq[pos-1]) = (seq[pos-1],seq[pos])
		pos = pos-1
	return(seq)

l2 = list(range(500,0,-1))
#print(RInsertionSort(l2))

#	Maximum Recursion Depth -Less than 10^4

#	Set Recursion Limit Manually for special programs.
#	import sys
#	sys.setrcursionlimit(10000) 

#	Complexity of Recurion insertion sort.
#	T(n) = O(n^2)	

##########################################################################
#####################	Programming Assignment	##########################

"""
	ASSIGNMENT Week 3 - SUBMITTED BY ADITHYA M.N. (RA1711018010088)

	1)	Write a function contracting(l) that takes as input a list of integer l and returns 
	True if the absolute difference between each adjacent pair of elements strictly decreases.

	Here are some examples of how your function should work.

		>>> contracting([9,2,7,3,1])
		True

		>>> contracting([-2,3,7,2,-1]) 
		False

  		>>> contracting([10,7,4,1])
  		False
"""
#	Solution

def contracting(l):						
    prev = abs(l[1] - l[0])
    i = 1
    while i < len(l)-1:
        if abs(l[i] - l[i+1]) < prev:
            i += 1
        else:
            break
    if i == len(l) - 1:
        return True
    return False

"""
2)	In a list of integers l, the neighbours of l[i] are l[i-1] and l[i+1]. l[i] is a hill if it 
	is strictly greater than its neighbours and a valley if it is strictly less than its neighbours.
	Write a function counthv(l) that takes as input a list of integers l and returns a list [hc,vc] 
	where hc is the number of hills in l and vc is the number of valleys in l.

	Here are some examples to show how your function should work.

 
		>>> counthv([1,2,1,2,3,2,1])
		[2, 1]

		>>> counthv([1,2,3,1])
		[1, 0]

		>>> counthv([3,1,2,3])
		[0, 1]
"""
# Solution

def counthv(l):
    count = [0, 0]
    for i in range(1, len(l) - 1):

        if l[i - 1] > l[i] < l[i + 1]:
            count[1] += 1

        elif l[i - 1] < l[i] > l[i + 1]:
            count[0] += 1

    return count
"""
#	3) A square n×n matrix of integers can be written in Python as a list with n elements, where each
	element is in turn a list of n integers, representing a row of the matrix. For instance, the matrix

  	1  2  3
  	4  5  6
  	7  8  9
	would be represented as [[1,2,3], [4,5,6], [7,8,9]].

	Write a function leftrotate(m) that takes a list representation m of a square matrix as input, and
	returns the matrix obtained by rotating the original matrix counterclockwize by 90 degrees. For instance,
	if we rotate the matrix above, we get

  	3  6  9
  	2  5  8    
  	1  4  7
	Your function should not modify the argument m provided to the function rotate().

	Here are some examples of how your function should work.

		>>> leftrotate([[1,2],[3,4]])
		[[2, 4], [1, 3]]

		>>> leftrotate([[1,2,3],[4,5,6],[7,8,9]])
		[[3, 6, 9], [2, 5, 8], [1, 4, 7]]

		>>> leftrotate([[1,1,1],[2,2,2],[3,3,3]])
		[[1, 2, 3], [1, 2, 3], [1, 2, 3]] 
"""
# Solution
def leftrotate(m):
    l = len(m)
    for i in range(l//2):
	for j in range(i, l-i-1):
        
	    temp = m[i][j]
	
            m[i][j] = m[j][l-i-1]
            m[j][l-i-1] = m[l-i-1][l-j-1]
            m[l-i-1][l-j-1] = m[l-j-1][i]
            m[l-j-1][i] = temp
    return m

##########################################################################
########################	End of Week 3	##########################
##########################################################################
