import Grader
import sys

f = str(sys.argv[1])+".py"

Student = "tmp/"+f
C = Grader.Checker("951196832","1",Student)
C.check()
for line in C.message:
	print ">"+str(line)


