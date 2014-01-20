import subprocess as sub

proc =  sub.Popen('python filer.py', shell = True, stdout = sub.PIPE, stdin = sub.PIPE, stderr = sub.PIPE, universal_newlines = True)
rawOut = proc.communicate(input='test.txt')	
stdout = rawOut[0].splitlines()rawOut[0].splitlines()
stderr = rawOut[1].splitlines()
print stdout