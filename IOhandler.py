import subprocess as sub
import collections
class IO:
    """
    Handles getting the inpout and output of test cases as well as runnning the student's code in a subprocess.
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
                line = str(line).rstrip()
                output.append(line)
            return output


    def getCases(self, ProblemNumber):
        """
        Returns the number of test cases for a given problem by traversing the directory.
        Uses lineReader to get number of cases from ProblemX/cases.txt file.
        """
        problem = "problems/"+"problem"+str(ProblemNumber) ##the problem number subdirectory
        casesFile = open(problem+"/cases.txt","r") ##the cases.txt file for the problem number
        cases = self.lineReader(casesFile,"int")
        return cases

    def getExpected(self,ProblemNumber,CaseNumber):
        """
        Returns the expected output of a specfic test case.
        Uses lineReader to get the expected output from problemX/cases/caseX/output.txt file
        """
        problem = "problems/"+"problem"+str(ProblemNumber)+"/" ##the problem number subdirectory
        filename = "output"+str(CaseNumber)+".txt"          ##the output.txt file for the case number
        expectedFile = open(problem+filename,'r')
        expected = self.lineReader(expectedFile,"list")
        return expected

    def getInput(self,ProblemNumber,CaseNumber):
        """
        Returns the input of a specfic test case.
        Uses lineReader to get the expected output from ProblemX/caseX/input.txt file
        """
        problem = "problems/"+"problem"+str(ProblemNumber)+"/" ##the problem number subdirectory
        filename = "input"+str(CaseNumber)+".txt"               ##the input.txt file for the case number
        inputFile = open(problem+filename,'r')
        Input = self.lineReader(inputFile,"string")
        return Input


    def OutputHandler(self, TestInput, studentCode):
        """
        Returns a named tuple structed as:
        (Type, output)

        Where type will be one of the following:
        error - the student's Code raised a stderr.
        loop  - the student's code passed the cpu time limit becasue of an inifnite loop.
        okay  - the student's code created an output normally.



        """

        FullInput = "ulimit -t 2; python3 " + str(studentCode) ##ulimit to prevent getting hung on inifinite loop.

        ## Run student's code
        proc =  sub.Popen( FullInput, shell = True, stdout = sub.PIPE, stdin = sub.PIPE, stderr = sub.PIPE, universal_newlines = True)

        ## Pass stdout and stderr to variables
        rawOut = proc.communicate(input=TestInput)	## passes TestInput as stdin; returns tuple (stdoutdata, stderrdata)
        stdout = rawOut[0].splitlines()
        stderr = rawOut[1].splitlines()

        studentOut = []
        errorDetails = []
        result = collections.namedtuple('result','type output')


        ## Put student's code into a list
        for line in stdout:
            studentOut.append(line)
          



        
        if stderr: ## if there's an error put in in errorDetails
           

            for line in stderr:
                errorDetails.append(str(line)) ## Put   stderr message in a list

            if "Killed" in errorDetails:
                ## Killed in stderr denotes that the student code exceeding cpu time limit
                return result("loop", errorDetails)

            else:
                return result("error",errorDetails)


        else:
            return result("okay",studentOut) ## if no error the student's output is okay
