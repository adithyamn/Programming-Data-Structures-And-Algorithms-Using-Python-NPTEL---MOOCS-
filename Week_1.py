					#############################
					#####	NPTEL - COURSE	#####
					#############################

#########################################################################
#####	Programming, Data Structures and Algorithms Using Python	#####
#########################################################################

############################	WEEK 1	#################################

#	NOTES

#	what is an algorithm? - Systematically perform a task.
#	what is a program? - Sequence of Steps to perform a task.
#	what is a step? - Degrees of details (depends on application).

#	What falls under algorithm's defeition?
#		1) Compute Numerical Functions - f(x,y) (algorithm)
#		2) Reorganise data - Arrange in ascending order. (data structures)
#		3) Optimisation - Find the Shortest Route - SPA, etc..

##############################################################################
###############	  Example 1 - Greatest Common Divisor	######################


#Defenitions - gcd(m,n) where,	gcd - greatest common divisor
#								m, n - numbers
#								k - largest number which divides both m and n
def naive_gcd(m,n):
	
	fm = []					# Factors of m
	for i in range(1,m+1):
		if(m%i) == 0:
			fm.append(i)

	fn = []					# Factors of n
	for j in range(1,n+1):
		if(n%j) == 0:
			fn.append(j)

	cf = []					# Common Factors of m and n
	for f in fm:
		if f in fn:
			cf.append(f)

	return(cf[-1]) #-1 returns the rightmost element of the array

def gcd(m,n):
	new_cf =[]
	for k in range(1, min(m,n)+1):
		if (m%k) == 0 and (n%k) == 0: #Finds the commonfactor
			cf.append(k)

	return(new_cf[-1])

def modified_gcd(m,n):

	for l in range(1,min(m,n)+1):
		if(m%l) == 0 and (n%l) == 0:
			mrcf = l
	return(mrcf)

	#	Euclid's Algorithm

#	If d divides both m and n and m>n
#	Then m = ad, n = bd
#	So m-n = (a-b)d
#	also, ad = qq(bd) + r where, r = cd

def eu_gcd(m,n):
	if m<n: #assume m>=n
		(m,n) = (n,m)

	while (m%n) != 0:
		(m,n) = (n, m%n) #m%n < n, always!

	return(n)

############################	End of Example 1	#########################
#############################################################################

#######################		WEEK 1 - QUIZ		#############################

# Question 1
def h(x):
    (d,n) = (1,0)
    while d <= x:
        (d,n) = (d*3,n+1)
    return(n)

ans1 = h(19685)
print(ans1)
#Ans1 - 10

# Question 2
def g(n): 
    s=0
    for i in range(2,n):
        if n%i == 0:
           s = s+1
    return(s)

ans2 = g(36) - g(35)
print(ans2)
#Ans - 5

#Question 3
def f(n): 
    s=0
    for i in range(1,n+1):
        if n//i == i and n%i == 0:
           s = 1
    return(s%2 == 1)

ans3 = f(144)
print(ans3)
#Ans - Returns true only if its a Perfect Square

#Question 4
def foo(m):
    if m == 0:
      return(0)
    else:
      return(m+foo(m-1))

ans4 = foo(5)
print(ans4)
#Ans - The function always terminates with f(n) = n(n+1)/2
