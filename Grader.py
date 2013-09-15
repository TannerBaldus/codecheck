import subprocess as sub
import collections
class IO:
	"""
	
	"""

	def lineReader(self, Input, type):
		"""
		Returns the content of an input (usually a file) into the specfied type

		"""

		if type == "string":
			output = ""
			for line in Input.readlines():
				output += (" " + line)
			return output 

		elif type == "int":
			for line in Input.readlines():
				output = int(line)
			return output

		elif type == "list":
			output = []
			for line in Input.readlines():
				output.append(str(line))
			return output


	def getCases(self, ProblemNumber):
		"""
		Returns the number of test cases for a given problem by traversing the directory.
		Uses lineReader to get number of cases from ProblemX/cases.txt file.
		"""
		problem = "problems/"+str(ProblemNumber)     
		casesFile = open(problem+"/cases.txt","r")
		cases = self.lineReader(CasesFile,"int")
		return cases

	def getExpected(ProblemNumber,CaseNumber):
		"""
		Returns the expected output of a specfic test case.
		Uses lineReader to get the expected output from ProblemX/caseX/output.txt file
		"""
		problem = "problems/"+str(ProblemNumber)
		case = "/case"+str(CaseNumber)
		expectedFile = open(problem+"/"+case+"/output.txt",'r')
		expected = self.lineReader(expectedFile,"list")
		return expected

	def getInput(ProblemNumber,CaseNumber):
		"""
		Returns the input of a specfic test case.
		Uses lineReader to get the expected output from ProblemX/caseX/input.txt file
		"""
		problem = "problems/"+str(ProblemNumber)
		case = "/case"+str(CaseNumber)
		inputFile = open(problem+"/"+case+"/input.txt",'r')
		Input = self.lineReader(inputFile,"list")
		return Input


	def OutputHandler(self, TestInput, studentCode,linelimit, message):
		"""
		Returns a named tuple structed as:
		(Type, output)

		Where type will be one of the following:
		error - the student's Code raised a stderr.
		loop  - the student's code passed the cpu time limit becasue of an inifnite loop.
		okay  - the student's code created an output normally.



		"""

		FullInput = "uliimit -t 2; python" + TestInput  
		proc =  sub.Popen( FullInput, shell = True, stdout = sub.PIPE, stderr = sub.PIPE)
		out = proc.stdout
		error = proc.stderr

		studentOut = []
		errorDetails = []
		returnValue = collections.namedtuple('Value',['type','output'])

		i = 0
		for line in out.readlines():
			studentOut.append(line)
			i += 1
			if i > linelimit:
				break
			

		if error != None:

			for line in error.readlines():

				if str(line.rstrip()) == "Killed":
					break
					return Value('loop','None')

				else:	
					errorDetails.append(str(line)
			
			return  Value("error",errorDetails)

		
		else:
			return Value("okay",studentOut) 



class Checker(object):
	"""
	Summary
	-------
	
	

	Methods
	--------
	init
	compare
	check



	"""
	def __init__(self, StudentId, ProblemNumber, sPudentCNode,linelimit):
		"""
		Initates class with a studentid number, a string as problem number, a path to the student's code file,  
		an empty list as message, and a boolean as correctFlag.

		Purpose of each variable:
		studentCode     =>  the path is used to run the Student's code using subprocess.Popen
		studentId       =>  used to generate a unique completeion token
		problemNumber   =>  used to get appropriate test cases
		linelimit		=>  used to specify number of lines of the  Student's code is allowed to produce. (see: ouputhandler)
		message			=>  each element in the list is a line to be displayed to student.
		correctFlag		=>  only stays true if the student's code passes each test case.

 		"""
		self.studentCode = studentCode
		self.StudentId = StudentId
		self.problemNumber = problemNumber
		self.linelimit = linelimit
		self.message = []
		self.correctFlag = True


	def compare(expected, given):
		"""
		Takes two lists as args, compares the two line by line and appends diffrences
		to self.message to be displayedto the student
		"""
		message = self.message
		i = 0
		for line in expected:
			if line != given[i]:
				message.append("Expected: "+str(line))
				message.append("Given:    "+str(given[i]))
				i += 1

	def check():
		problem = self.problem

		IO = IO()
		for i in range(IO.getCases(problem)):

			caseNumber = i
			caseInput = IO.getInput(problem, caseNumber)
			expected = IO.getExpected(problem,caseNumber)
			codeResult = IO.OutputHandler(caseInput, self.studentCode,self.linelimit)

			if codeResult == "loop":
				selage.append("Your script exceeded the cpu time limit.")
				self.message.append("This is most likley due to an infnite loop.")
				self.message,append("Check your for and while loops.")
				self.message("Sometimes you just put a '>' instead of a '<' or forgot to iterate ex: i += 1.")
				break

			elif codeResult.type == "error":
				self.e.append("Input: "+ caseInput)
				self.message.extend(codeResult.output)
				

			elif codeResult.type == okay:
				given = codeResult.output

				lenDiff = len(expected) - len(given)

				tooLong = lendiff < 0			## the given output is too long
				tooShort = lendiff > 0			## the given output is too short

				if tooLong:
					tail = len(expected)
					comparableGiven = given[0:tail] 		## makes given the same length as expected
					leftOver = given[tail:]					## the rest of given output

					self.compare(expected,comparableGiven)	

				elif tooShort:
					tail = len(expected)
					comparableExpected = expected[0:tail] 		## makes the expected output the same length as given
					leftOver = expected[tail:]					## the rest of the expected output

					self.compare(expected,comparableGiven)

				else:
					self.compare(expected,given)	












			
