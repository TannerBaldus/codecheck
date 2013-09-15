import subprocess as sub
from collections import namedtuple
class IO:
    """

    """

    def lineReader(self, Input, type):
        """
        Returns the content of an input (usually a file) into the specfied type

        """

        if type == "string":
            output = ""
            for line in Input.readlines():
                output += (" " + line)
            return output

        elif type == "int":
            for line in Input.readlines():
                output = int(line)
            return output

        elif type == "list":
            output = []
            for line in Input.readlines():
                output.append(str(line))
            return output


    def getCases(self, ProblemNumber):
        """
        Returns the number of test cases for a given problem by traversing the directory.
        Uses lineReader to get number of cases from ProblemX/cases.txt file.
        """
        problem = "problems/"+"problem"+str(ProblemNumber)
        casesFile = open(problem+"/cases/cases.txt","r")
        cases = self.lineReader(casesFile,"int")
        return cases

    def getExpected(self,ProblemNumber,CaseNumber):
        """
        Returns the expected output of a specfic test case.
        Uses lineReader to get the expected output from problemX/cases/caseX/output.txt file
        """
        problem = "problems/"+"problem"+str(ProblemNumber)
        case = "/cases/case"+str(CaseNumber)
        expectedFile = open(problem+"/"+case+"/output.txt",'r')
        expected = self.lineReader(expectedFile,"list")
        return expected

    def getInput(self,ProblemNumber,CaseNumber):
        """
        Returns the input of a specfic test case.
        Uses lineReader to get the expected output from ProblemX/caseX/input.txt file
        """
        problem = "problems/"+"problem"+str(ProblemNumber)
        case = "/cases/case"+str(CaseNumber)
        inputFile = open(problem+"/"+case+"/input.txt",'r')
        Input = self.lineReader(inputFile,"list")
        return Input


    def OutputHandler(self, TestInput, studentCode,linelimit, message):
        """
        Returns a named tuple structed as:
        (Type, output)

        Where type will be one of the following:
        error - the student's Code raised a stderr.
        loop  - the student's code passed the cpu time limit becasue of an inifnite loop.
        okay  - the student's code created an output normally.



        """

        FullInput = "ulimit -t 2; python" + str(studentCode)

        ## Run student's code
        proc =  sub.Popen( FullInput, shell = True, stdout = sub.PIPE, stderr = sub.PIPE, universal_newlines = True)

        ## Pass stdout and stderr to variables
        rawOut = proc.communicate(input=TestInput)	## passes TestInput as std in; returns tuple (stdoutdata, stderrdata)
        stdout = rawOut[0].splitlines()
        stderr = rawOut[1].splitlines()

        studentOut = []
        errorDetails = []
        returnValue = collections.namedtuple('Value','type output')


        ## Put student's code into a list
        i = 0
        for line in stdout:
            studentOut.append(line)
            i += 1
            if i > linelimit:
                break


        ## Put 	stderr message in a list
        if stderr != None:

            for line in stderr():

                if str(line.rstrip()) == "Killed":
                    ## Killed in stderr denotes the Student's Code surpassed the cpu time limit
                    break
                    return Value('loop','None')

                else:
                    errorDetails.append(str(line)
                    return Value("error",errorDetails)


        else:
            return Value("okay",studentOut)
            