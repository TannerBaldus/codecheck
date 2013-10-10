import hashlib
class Token(object):
	def __init__(self,studentId,correctFlag):
		self.studentId = studentId
		self.correctFlag = correctFlag
		self.salt = ""

	def generateToken(self):
		message = []
		token = hashlib.md5(self.studentId+self.salt)
		if self.correctFlag == True:
			token.update("correct")
			message.append("Congrats you got it right! Here's your token: ")
			message.append(token.hexdigest())
		else:
			token.update("wrong")
			message.append("Sorry your code didn't pass all of the test cases see below for what went wrong.")
			message.append("You still get a token for trying: ")
			message.append(token.hexdigest())
	
		return message



