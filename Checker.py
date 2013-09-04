import subprocess as sub
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
	def __init__(self, StudentId, problem, StudentCode):
		"""
		Initates class with a studentid number, problem.obj file, a StudentCode.py file and 
		a empty message string.
		"""
		self.StudentCode = StudentCode
		self.StudentId = StudentId
		self.problem = problem
		self.message = ""
		self.CorrectFlag = True

	def OutputHandler(self, TestInput,StudentCode,ExpectedOut):
		"""

		"""
		FullInput = TestInput.extend(StudentCode)
		RawOut =  sub.Popen( FullInput, stdout = sub.PIPE, stderr = sub.PIPE)
		StudentOut = []

		if RawOut.stderr:
			for line in RawOut.stderr.readlines():
				self.message.append(line)
			return "error"

		else:
			for line in RawOut.readlines():
				StudentOut.append(line)

			return "okay" 

