import subprocess as sub


FullInput = "ulimit -t 2; python " + "test.py "+"hello world"
## Run student's code
proc =  sub.Popen( FullInput, shell = True, stdout = sub.PIPE, stdin =sub.PIPE, stderr = sub.PIPE, universal_newlines = True)

## Pass stdout and stderr to variables
rawOut = proc.communicate(input="hello world")	## passes TestInput as stdin; returns tuple (stdoutdata, stderrdata)
stdout = rawOut[0].splitlines()
stderr = rawOut[1].splitlines()

print "fuck me right"
print stdout
for line in stdout:
	print line