			#############################
			#####	NPTEL - COURSE	#####
			#############################

#########################################################################
#####	Programming, Data Structures and Algorithms Using Python    #####
#########################################################################

############################	WEEK 2	#################################

#########################################################################
###  Lecture 1: Assignment statement, basic types - int, float, bool  ###
#########################################################################

#	NOTES

#	How a typical python program works!
#	What is a Statement? - Assign a value to a name/variable.
#	For Eg :	j = 2
#				j = j + 5
#	Here, LHS is the Name , RHS is the Expression
#	Operations Available to the expression depends on the TYPE of expression.

#	TYPES OF NUMERIC VALUES

#		int - Integers
#		float - Fractional Numbers

#	0.602 * 10^24 <---- Exponent
#	  ^
#	  |
#	Mantissa

#	OPERATIONS ON NUMERIC VALUES
#		Normal Operations - " + , - , * , / "
#		Quotient " // " and Remainder " % "
#		log() , sqrt() , sin() - Math Library

#	type(e) - returns the type of expression "e"

#	Boolean Values -  True, False
#	Logical Operators - not , and , or

#	Some Comparators
#		x == y, a!= b
#		z < 3*4 , n > m
#		i <= j+k , 19 >= 44*d

print("Example 1")
def divides(m,n):
	if n%m == 0:
		return(True)
	else:
		return(False)
 
d = divides(3, 27)
print (d)
print(type(d))

###########################################################################
########################  Lecture 2: Strings  #############################
###########################################################################

#	Notes

# 	str = string - a sequence of charaters
#	s = "hello"
#	s[1] == "e" Extracting strings

#	" + " concatenates 2 or more strings

#	len(s) - Lenght of string s

#	slice - extracts a substring of a string
#	s[1:4] is "ell"
#	s[:j] - from the begenning of string to j
#	s[i:] - from i to the end of string

#	We can modify strings but slicing them and concatenating them.

s = "hello"
print(s[1:4]);
print(s[:2] + "ro");
print(s[0:len(s)]);

###########################################################################
########################  Lecture 3: Lists	  #########################
###########################################################################

#	Notes

#	Lists
#	Key difference :	factors = [1,2,5,10]
#						factors[0] == 1 <-- This is a value
#						factors[0:1] == [1] <-- This is a list

#	Nested List :	

nested = [[2,[37,7]], 4 , ["hello"]]

print(nested[0])
print(nested[1])
print(nested[2][0][3])
print(nested[0][1:2])

#	Mutable Listes

nested[0][1][0] = 19
print(nested)

#	Other variables get affected if a list is muted.
#		how to overcome this?
#		Use l[:] - Full Slice
#		list2 = list1[:]
#	Now the different lists will not get affected by one another.

list1 = [1,3,5,7]
list2 = [1,3,5,7]
list3 = list2

#	Digression on Equality

print(list1 == list2)
print(list2 == list3)

print(list1 is list2)
print(list2 is list3)

#	List Concatenation

list2 = list2 + list3
print(list1)

#Decoupling of Lists when concatenated
print(list2 is list3)

###########################################################################
########################  Lecture 4: Control Flow  ########################
###########################################################################

#	Notes
#	if m%n != 0:
#		(m,n) = (n,m%n)
#	second statement is only executed if the condition is true.

#	Indentation Demarcates the Body

#	if condition:
#		statement1
#		statement2
#	statement3

#	statement 1 & 2 gets executed only if condition is true.
#	statement 3 gets executed regardless	

#	Conditional Statements
#	Loops

#	for i in [1,2,3,4]: == for i in rangr(0,n):

def factor(n):
	flist = []
	for i in range(1,n+1):
		if n%i == 0:
			flist = flist + [i]
	return(flist)

print(factor(10))

#	Entry Controlled Loop  - While
#	Exit controlled Loop - For

###########################################################################
########################  Lecture 5: Funcitons	  #########################
###########################################################################

#	def f(a,b,c)
#		statement1
#		statement2
#		return(v) where v is a constant generally

#	1
def power(x,n):
	ans = 1
	for i in range(0,n):
		ans = ans*x
	return(ans)

print(power(3,5))

#	2
def f(x):
	return (g(x+1))
def g(y):
	return(y+3)

print(f(77))

#	Sideeffects occur in mutable values in funnctions
#	A funtction which can call itself is RECURSIVE.

##########################################################################
#############################	Examples    ##############################

#	Find the factors of a number n

def factors(n):
	factorlist = []
	for i in range(1,n+1):
		if n%i == 0:
			factorlist = factorlist +[i]
	return(factorlist)

print(factors(25))

#	Find whether a number is prime or not

def isprime(n):
	return(factors(n) == [1,n])

print(isprime(17))

#	Find the number of primes upto n

def primesupto(n):
	primelist = []
	for i in range(1,n+1):
		if isprime(i):
			primelist = primelist + [i]
	return(primelist)

print(primesupto(100))

#	Find the first n primes

def nprimes(n):
	(count, i, plist) = (0,1,[])
	while(count< n):
		if isprime(i):
			(count,plist) = (count+1, plist+[i])
		i= i+1
	return(plist)

print(nprimes(10))


###########################	End of Examples	    ######################
##########################################################################

#######################		WEEK 2 - QUIZ	##########################

#	1)
x = ["slithy",[7,10,12],2,"tove",1]  # Statement 1
y = x[0:50]                          # Statement 2
z = y                                # Statement 3
w = x                                # Statement 4
x[0] = x[0][:5] + 'ery'              # Statement 5
y[2] = 4                             # Statement 6
z[4] = 42                            # Statement 7
#w[0][:3] = 'fea'                     # Statement 8
x[1][0] = 5555                       # Statement 9
#a = (x[4][1] == 1)                   # Statement 10

#	Ans : Statement 8 Reason : Item Assignment is not possible for string

#	2)
b = [23,44,87,100]
a = b[1:]
d = b[2:]
c = b
d[0] = 97
c[2] = 77

print([a[1], b[2], c[2], d[0]])

# Ans - [87, 77, 77, 97]

#	3)
startmsg = "python"
endmsg = ""
for i in range(1,1+len(startmsg)):
  endmsg = startmsg[-i] + endmsg

print(endmsg)

#	Ans - python

#	4)
def mystery(l):
  l = l[1:]
  return()

mylist = [7,11,13]
mystery(mylist)

print(mylist)

#	Ans - [7, 11, 13]

##########################################################################
#####################	Programming Assignment	##########################

#	ASSIGNMENT - SUBMITTED BY ADITHYA M.N. (RA1711018010088)

#	1) Product Prime
#	A positive integer m is a prime product if it can be written as p×q, where p and q are both primes.
#	Write a Python function primeproduct(m) that takes an integer m as input and returns 
#	True if m is a prime product and False otherwise. (If m is not positive, your function should return False.)

def primeproduct(m):
    product=1
    for i in range(2,(m//2)+1):		#we only want prime number which is a factor of "m"
        if(m%i==0 and m>=0):		#to check whether "i" is a factor of m or not
            product*=i
    if(product==m):
        return(True)			#like if u give input a 188. so factor of 188 r 2,4,47,94 and  when u divde 188 by 2 u will get 94. After than when u call function 
    else:				#u will never get "product == m"
        return(False)
print(primeproduct(202))

#	2)Write a function delchar(s,c) that takes as input strings s and c, where c has length 1 
#	(i.e., a single character), and returns the string obtained by deleting all occurrences of 
#	c in s. If c has length other than 1, the function should return s

def delchar(s,c):
	if len(c) > 1:				#	Considering the case where the length of c is not 1
		return(s)
	elif len(c) == 1:
		for i in s:					#	Iterating through all characters in string
			if i is c:				#	Finding all the character in string with s
				new_s = s.replace(i,"")	#	Replacing the value
	elif len(c) < 1:
		return("Character Is Null")
	else:
		return("Character Given is not in the word") #Considering invalid case.
	return(new_s)

print(delchar("banana", ""))

#	3) Write a function shuffle(l1,l2) that takes as input two lists, 11 and l2, and returns 
#	a list consisting of the first elment in l1, then the first element in l2, then the second 
#	element in l2, then the second element in l2, and so on. If the two lists are not of equal 
#	length, the remaining elements of the longer list are appended at the end of the shuffled output.

def shuffle(l1, l2):
	new_l = []								#Initialising Variables
	j= 0
	k= 0
	for i in range (0,len(l1)+len(l2)):		#	Runs through the loop for the total length
	#	Checking if the iteration number is odd or even we do this so that we can add elements
	#	fromboth lists at alternate iteration "even" for appending elements from list1 and "odd"
	#	appending elements from list2
	#	Control Flow loop for appropriate append usage to get the correct output
		if i%2 == 0:						
			if(j< len(l1)):					
				new_l.append(l1[j])
				j += 1
			else:
				new_l.append(l2[k])
				k += 1

		elif i%2 != 0:
			if(k< len(l2)):
				new_l.append(l2[k])
				k += 1
			else:
				new_l.append(l1[j])
				j += 1
			
	return(new_l)
x = shuffle([0,5,4,5],[1,2,3,6,7,9])
print(x)
