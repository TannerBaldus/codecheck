import sys

filen = sys.stdin.readline().strip()
print filen

fn = open(filen)

for line in fn.readlines():
	print(line.strip())
