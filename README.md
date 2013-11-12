CodeCheck
=========

A webapp for checking student code against an expected output of multiple test cases.
Codecheck runs student submitted python scripts in a subprocess and compares the output produced against a given output.

How to use:
-----------
>Move the CodeCheck folder to your cgi-bin directory.

>Create problem pages using the problem template provided. Or any sort of HTML implmentation as long as it has a form that posts
a student ID and  python file as well as a get method to pass the problem number to main.cgi. You can link to these pages however you wish

>To add input and output for a problem:

	navigate to the appropriate prroblem directory, for example problem1 would be:
		codecheck/problems/problem1

	create a cases.txt with the amount of test cases you want to run ex:
		in cases.txt:
			2

	create input.txt and output.txt files numbered 0 - number of cases -1.
	for 2 test cases this would look like:
	input0.txt input1.txt output0.txt output1.txt

>That's it.