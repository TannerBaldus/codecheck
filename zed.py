import sys
class Zombie:

	def __init__(self,input_name,input_moan):
		self.name = input_name
		self.moan = input_moan


	def identify(self):
		"""
		prints exactly of the form:

		moan My name moan is name 
		"""
		print(self.moan +" My name "+self.moan+" is "+self.name)

		

	def getName(self):
		""" Returns the name of the zombie"""
		return self.name



class Human:
	"""
	Initalized with a name and and an instance of Zombie that it is 
	being chased by.
	"""

	def __init__(self,input_name, zombie):
		self.name = input_name
		self.chased_by = zombie

	def identify(self):
		"""
		prints exactly of the form

		My name is name I'm being chased by zombie name

		"""
		print("My name is "+self.name+ " I'm being chased by "+ self.chased_by.getName())


def main():
	args = sys.stdin.readline().rstrip()
	args = args.split()
	zombie_name = args[0]
	zombie_moan = args[1]
	human_name = args[2]


	z = Zombie(zombie_name, zombie_moan)
	h = Human(human_name,z)
	z.identify()
	h.identify()
	
if __name__ == '__main__':
	main()










