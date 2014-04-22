import sys
class Zombie:
	"""
	Instantiated with a name and moan

	Variables:
	moan = string of zombie moan
	name = string of the zombie's name

	Methods:
	__init__
	identify
	get_name
	"""

	def __init__(self,input_name,input_moan):
		self.name = input_name
		##initalize moan


	def identify(self):
		"""
		prints exactly of the form:

		moan My name moan is name 
		"""
		print("FIXME" +" My name "+"FIXME"+" is "+"FIXME")

		

	def get_name(self):
		""" Returns the name of the zombie"""
		return self.name



class Human:
	"""
	Initalized with a name and and an instance of Zombie that it is 
	being chased by.

	Variables:
	name    = string 
	chased_by = instance of Zombie

	Methods:
	__init__
	identify

	"""

	def __init__(self,input_name, zombie):
		pass
		##initalize name
		##initialize chased_by

	def identify(self):
		"""
		prints exactly of the form

		My name is name I'm being chased by zombie name

		"""
		print("My name is "+"FIXME"+ " I'm being chased by "+ "FIXME")


def main():
	args = sys.stdin.readline().rstrip()
	args = args.split()
	zombie_name = args[0]
	zombie_moan = args[1]
	human_name = args[2]


	##create an instance of zombie
	##create an instance of human
	##make the zombie identify
	##make the human identify
	
if __name__ == '__main__':
	main()





