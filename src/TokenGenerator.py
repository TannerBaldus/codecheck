import hashlib
class Token(object):
	"""
	Creates a token unique to the student's Id, problem number, and correctness of output. 
	Appends the generated token after a congratulatory or conciliatory message.
	"""
	def __init__(self,studentId,correctFlag):
		self.studentId = studentId
		self.correctFlag = correctFlag
		self.salt = ""

	def generateToken(self):
		message = []
		token = hashlib.md5(self.studentId+self.salt)
		if self.correctFlag == True: ## the student passed all of the test cases
			token.update("correct")
			message.append("Congrats you got it right! Here's your token: ")
			message.append(token.hexdigest())
		else: ## the student did not pass all of the test cases
			token.update("wrong") 
			message.append("Sorry your code didn't pass all of the test cases see below for what went wrong.")
			message.append("You still get a token for trying: ")
			message.append(token.hexdigest())
	
		return message



