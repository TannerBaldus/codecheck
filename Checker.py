import subprocess as sub
import collections
class IO:

	def lineReader(self, Input, type):

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
		problem = "problems/"+str(ProblemNumber)
		casesFile = open(problem+"/cases.txt","r")
		cases = self.lineReader(CasesFile,"int")
		return cases

	def getExpected(ProblemNumber,CaseNumber):
		problem = "problems/"+str(ProblemNumber)
		case = "/case"+str(CaseNumber)
		expectedFile = open(problem+"/"+case+"/output.txt",'r')
		expected = self.lineReader(expectedFile,"list")
		return expected

	def getInput(ProblemNumber,CaseNumber):
		problem = "problems/"+str(ProblemNumber)
		case = "/case"+str(CaseNumber)
		inputFile = open(problem+"/"+case+"/input.txt",'r')
		Input = self.lineReader(inputFile,"list")
		return Input


	def OutputHandler(self, TestInput, StudentCode,linelimit, message):
		"""

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
	Contains methods to check students code against an expceted output. Multiple expected outputs from multiple text cases are given as a dictonary as a .obj file. The .obj files are read using the pickle module.
	Each test case (numbered 0 to n) is a key corresponding to a list with input as the first element and the rest of the elements as each line of the excpected output.
	 	example:
	 	dict = [0:[input,"hello world", "goodbye cruel world"]]

	

	Methods
	--------
	OutputHandler


	"""
	def __init__(self, StudentId, problem, StudentCode,linelimit):
		"""
		Initates class with a studentid number, problem.obj file, a StudentCode.py file and 
		a empty message string.
		"""
		self.StudentCode = StudentCode
		self.StudentId = StudentId
		self.problem = problem
		self.linelimit = linelimit
		self.message = []
		self.CorrectFlag = True


	def compare(expected, given):
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
			codeResult = IO.OutputHandler(caseInput, self.StudentCode,self.linelimit)

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
				given = codeResult.o


			
