			#############################
			#####	NPTEL - COURSE	#####
			#############################

#########################################################################
#####	Programming, Data Structures and Algorithms Using Python    #####
#########################################################################

############################	WEEK 4	#################################

# NOTES REMOVED

#######################	WEEK 4 - QUIZ	##########################
"""
1) Consider the following Python function.
def mystery(l):
    if l == []:
        return(l)
    else:
        return(mystery(l[1:])+l[:1])
What does mystery([22,14,19,65,82,55]) return?
[55, 82, 65, 19, 14, 22]
Yes, the answer is correct.
Score: 2.5

2) What is the value of pairs after the following assignment?
pairs = [ (x,y) for x in range(4,1,-1) for y in range(5,1,-1) if (x+y)%3 == 0 ]
[(4, 5), (4, 2), (3, 3), (2, 4)]
Yes, the answer is correct.
Score: 2.5
2.5 points

3) Consider the following dictionary.
wickets = {"Tests":{"Kumble":[3,5,2,3],"Srinath":[4,4,1,0],"Prasad":[2,1,7,4]},"ODI":{"Kumble":[2,0],"Srinath":[1,2]}}
Which of the following statements does not generate an error?
 wickets["ODI"]["Prasad"][0:] = [4,4]
 wickets["ODI"]["Prasad"].extend([4,4])
 wickets["ODI"]["Prasad"] = [4,4]
 wickets["ODI"]["Prasad"] = wickets["ODI"]["Prasad"] + [4,4]
Yes, the answer is correct.
Score: 2.5


4) Assume that hundreds has been initialized as an empty dictionary:
hundreds = {}
Which of the following generates an error?
 hundreds["Tendulkar, international"] = 100
 hundreds["Tendulkar"] = {"international":100}
 hundreds[("Tendulkar","international")] = 100
 hundreds[["Tendulkar","international"]] = 100
Yes, the answer is correct.
Score: 2.5

"""

##########################################################################
#####################	Programming Assignment	##########################

"""
1) Write a Python function frequency(l) that takes as input a list of integers and returns a pair of the form (minfreqlist,maxfreqlist) where

minfreqlist is a list of numbers with minimum frequency in l, sorted in ascending order
maxfreqlist is a list of numbers with maximum frequency in l, sorted in ascending order
Here are some examples of how your function should work.

>>> frequency([13,12,11,13,14,13,7,11,13,14,12])
([7], [13])

>>> frequency([13,12,11,13,14,13,7,11,13,14,12,14,14])
([7], [13, 14])

>>> frequency([13,12,11,13,14,13,7,11,13,14,12,14,14,7])
([7, 11, 12], [13, 14])

"""
#	ASSIGNMENT Week 4 - SUBMITTED BY ADITHYA M.N. (RA1711018010088)

def frequency(lst):
  freq = dict()
  for i in lst:
    freq[i] = freq.get(i,0)+1
  mini = list()
  maxi = list()
  max = 0
  min = freq[lst[0]]

  for v in freq:
      if max < freq[v]:
          max = freq[v]

      if min > freq[v]:
          min = freq[v]

  for k,v in freq.items():
      if max == v:
          maxi.append(k)
      if min == v:
          mini.append(k)

  return (sorted(mini),sorted(maxi))

x = frequency([13,12,11,13,14,13,7,11,13,14,12])
print(x)


"""
2) An airline has assigned each city that it serves a unique numeric code. It has collected information about all the direct flights it operates, represented as a list of pairs of the form (i,j), where i is the code of the starting city and j is the code of the destination.

It now wants to compute all pairs of cities connected by one intermediate hope — city i is connected to city j by one intermediate hop if there are direct flights of the form (i,k) and (k,j) for some other city k. The airline is only interested in one hop flights between different cities — pairs of the form (i,i) are not useful.

Write a Python function onehop(l) that takes as input a list of pairs representing direct flights, as described above, and returns a list of all pairs (i,j), where i != j, such that i and j are connected by one hop. Note that it may already be the case that there is a direct flight from i to j. So long as there is an intermediate k with a flight from i to k and from k to j, the list returned by the function should include (i,j). The input list may be in any order. The pairs in the output list should be in lexicographic (dictionary) order. Each pair should be listed exactly once.

Here are some examples of how your function should work.

 
>>> onehop([(2,3),(1,2)])
[(1, 3)]

>>> onehop([(2,3),(1,2),(3,1),(1,3),(3,2),(2,4),(4,1)])
[(1, 2), (1, 3), (1, 4), (2, 1), (3, 2), (3, 4), (4, 2), (4, 3)]

>>> onehop([(1,2),(3,4),(5,6)])
[]

"""

def onehop(lst):
    li =[]
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i][0] != lst[j][1] and lst[i][1]==lst[j][0] :
                    li.append((lst[i][0],lst[j][1]))
    li = list(set(li))
    li = sorted(li)

    return li

y = onehop([(2,3),(1,2)])
print(y)
