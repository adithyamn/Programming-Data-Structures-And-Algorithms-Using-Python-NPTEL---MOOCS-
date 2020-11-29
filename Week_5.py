					#############################
					#####	NPTEL - COURSE	#####
					#############################

#########################################################################
#####	Programming, Data Structures and Algorithms Using Python	#####
#########################################################################

############################	WEEK 5	#################################
#########################################################################
##################  Lecture 1: Exception Handling  		#################
#########################################################################

"""
Notes
Exception = Error Visualising the error (debugging)
Catch the error without stopping the program.

Types of Error :
->	Name Error
->	ZeroDivision Error
->	Index Error

Terminology
Raise an Exception - Handle the Error.
Handle an Exception - Give Handle Code.

Handling Exceptions :

try:

except IndexError:
except (NameError, KeyError):
except:

else:
		<-- Executes Normally if try terminates (no errors.)

Traditional Approach:

scores = {'Dhawan': [3,22], 'Kohli':[200,3]}
If Batsman 'b' exists 
scores[b].append(s)
else
scores[b] = [s]

Using Exceptions

try:
	scores[b].append[s]
except KeyError:
	scores[b] = [s]
"""
#########################################################################
#############  	Lecture 2: Standard Input And Output		  ###########
#########################################################################

#	userdata = input("GGWP: ")
"""
while(True):
	try:
		userdata = int(input("Enter a Number : "))
		print(userdata)
	except ValueError:
		print("Not a Number. Try Again")
	else:
		print("Program Ended ")
		break
"""
#	Fine Tuning Print
print("Continue on the", end=" ")
print("same line", end=".\n")
print("NextLine.")

#########################################################################
#############  		Lecture 3: Handling Files			#################
#########################################################################

#	Reading writing disk data

#	Flushes the buffer, therfore not manipulaitng files.

#	Opening a File
#	fh = open("gcd.py", "r")

#	r - read
#	w - write
#	a - append

#	SOME OPERTATIONS
#	contents = fh.read()
#	contents = fh.readline()
#	contents = fh.readlines()
#	fh.seek(n)
#	block = fh.read(12)
#	fh.writelines(s)

#########################################################################
#############  		Lecture 4: String Processing		#################
#########################################################################

#	s.rstrip() - Removes Trailing Whitespaces
#	s.lstrip() - Removes Leading Whitespaces
#	s.strip() - Removes both spaces

#	Searching

#	s.find(pattern) - Returns first position in s wherer the pattern occurs
#	s.find(pattern, start, end)

#	Search and Replace

#	s.replce(fromstr, tostr, occurnace number)

#	Splits the list into separate array elements
#	columns = s.split(",")

#	Converting Cases

#	s.capitalisze()
#	s.lower() 
#	s.upper
#	s.title()

#	Resizing Strings

#	s.center(n,'something')	# Centers s in n strings
#	s.isaplha()
#	s.isnumeric()


#########################################################################
#############  		Lecture 5: Formatted Printing		#################
#########################################################################

#	format() 
#	>>> "First: {0}, second: {1}".format(47, 11)
#	>>> "First: {f}, second: {s}".format(f= 47, s= 11)
#	>>>	"Value: {0:3d}.format(4)"
#			d - Decimal
#			3 - width of the area to show 4
#			Also : .2f - Float to two decimals

#Lookup python formattting for more information.

#########################################################################
#############  		Lecture 6: Pass, del() and None		#################
#########################################################################
"""
	while(True):
		try:
		userdata = input("Enter a number: ")
			usernum = int(userdata)
		except ValueError:
			pass
			print("Not a Number : Try Again")
		else:
			break

	Remove a list Entry
	del(l[4])

	The Value None : 
	
	x = None

	if x is not None:
		y = x
"""
##########################################################################
#####################	Programming Assignment	##########################

#	ASSIGNMENT - SUBMITTED BY ADITHYA M.N. (RA1711018010088)

"""
The academic office at the Hogwarts School of Witchcraft and Wizardry has compiled data about students' grades. The data is provided as text from standard input in three parts: information about courses, information about students and information about grades. Each part has a specific line format, described below..

Information about courses
Line format: Course Code~Course Name~Semester~Year~Instructor
Information about students
Line format: Roll Number~Full Name
Information about grades
Line format: Course Code~Semester~Year~Roll Number~Grade
The possible grades are A, AB, B, BC, C, CD, D with corresponding grade points 10, 9, 8, 7, 6, 5 and 4. The grade point average of a student is the sum of his/her grade points divided by the number of courses. For instance, if a student has taken two courses with grades A and C, the grade point average is 8.50 = (10+7)÷2. If a student has not completed any courses, the grade point average is defined to be 0.

You may assume that the data is internally consistent. For every grade, there is a corresponding course code and roll number in the input data.

Each section of the input starts with a line containing a single keyword. The first section begins with a line containing Courses. The second section begins with a line containing Students. The third section begins with a line containing Grades. The end of the input is marked by a line containing EndOfInput.

Write a Python program to read the data as described above and print out a line listing the grade point average for each student in the following format:

Roll Number~Full Name~Grade Point Average
Your output should be sorted by Roll Number. The grade point average should be rounded off to 2 digits after the decimal point. Use the built-in function round().
"""
# Convert letter grade to grade point
def gradetonum(grade):
    if grade == 'A':
        return(10)
    elif grade == 'AB':
        return(9)
    elif grade == 'B':
        return(8)
    elif grade == 'BC':
        return(7)
    elif grade == 'C':
        return(6)
    elif grade == 'CD':
        return(5)
    elif grade == 'D':
        return(4)
    else:
        return(0)
                   
# Set up three dictionaries to store data
rollname = {}    # Key: roll number, Value: Name
gradepoint = {}  # Key: roll number, Value: Cumulative grade points
coursecount = {} # Key: roll number, Value: Number of courses taken

nextline = input().strip()
while nextline.find("Courses") < 0:
    nextline = input().strip()

# Read course data
while nextline.find("Students") < 0:
    nextline = input().strip()
    # Course data is irrelevant for this problem!

# Read students data
nextline = input().strip()
while nextline.find("Grades") < 0:
    fields = nextline.split('~')
    roll=fields[0]
    name=fields[1]
    rollname[roll] = name   # Initialize
    gradepoint[roll] = 0    # Initialize
    coursecount[roll] = 0   # Initialize
    nextline = input().strip()

# Read grades data
nextline = input().strip()
while nextline.find("EndOfInput") < 0:
    fields = nextline.split('~')
    roll=fields[3]
    grade=fields[4]
    gradepoint[roll] += gradetonum(grade)  # Update
    coursecount[roll] += 1                 # Update
    nextline = input().strip()

# Print output
for roll in sorted(rollname.keys()):
    if coursecount[roll] > 0:
        gpa = round(gradepoint[roll]/coursecount[roll],2)
    else:
        gpa = 0
    print(roll,rollname[roll],gpa,sep='~',end='\n' )
