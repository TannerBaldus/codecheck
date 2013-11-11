import sys
import subprocess as sub
code = sys.argv[1]+".py"
TestInput = "foo"
FullInput = "ulimit -t 2; python3 hello.py" 
proc =  sub.Popen( FullInput, shell = True, stdout = sub.PIPE, stderr = sub.PIPE)

## Pass stdout and stderr to variables
rawOut = proc.communicate(input=TestInput)	## passes TestInput as std in; returns tuple (stdoutdata, stderrdata)
stdout = rawOut[0].splitlines()

for line in stdout:
	printstr(line)
