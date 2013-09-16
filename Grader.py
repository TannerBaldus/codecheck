import IOhandler


class Checker(object):
    """
    Summary
    -------



    Methods
    --------
    init
    compare
    check



    """
    def __init__(self, studentId, problemNumber, studentCode,):
        """
        Initates class with a studentid number, a string as problem number, a path to the student's code file,
        an empty list as message, and a boolean as correctFlag.

        Purpose of each variable:
        studentCode     =>  the path is used to run the Student's code using subprocess.Popen
        studentId       =>  used to generate a unique completeion token
        problemNumber   =>  used to get appropriate test cases
        lineLimit		=>  used to specify number of lines of the  Student's code is allowed to produce. (see: ouputhandler)
        message			=>  each element in the list is a line to be displayed to student.
        correctFlag		=>  only stays true if the student's code passes each test case.

        """
        self.studentCode = studentCode
        self.studentId = studentId
        self.problemNumber = problemNumber
        self.message = []
        self.correctFlag = True

        ###### Setters and Getters######
    def getStudentCode(self):
        """ Returns student code """
        return self.studentCode

    def getStudentId(self):
        """ Returns studentId"""
        return self.studentId

    def getStudentCode(self):
        """ Returns student code """
        return self.studentCode

    def getProblemNumber(self):
        """Returns problem number."""
        return self.problemNumber

    def getMessage(self):
        """Returns message"""
        return self.message

    def setMessage(self,Input):
        if type(Input) == list:
            self.message.extend(list)
        else:
            self.message.append(Input)




    ##def get


    def compare(self,expected, given):
        """
        Takes two lists as args, compares the two line by line and appends diffrences
        to self.message to be displayedto the student
        """
        message = self.message
        i = 0
        for line in expected:
            if line != given[i]:
                message.append("Expected: "+str(line))
                message.append("Given:    "+str(given[i]))
                i += 1

    def check(self):
        problem = self.getProblemNumber()
        IO = IOhandler.IO()

        for i in range(IO.getCases(problem)):

            caseNumber = i
            caseInput = IO.getInput(problem, caseNumber)
            expected = IO.getExpected(problem,caseNumber)
            codeResult = IO.OutputHandler(caseInput, self.studentCode,self.lineLimit)

            if codeResult.type == "loop":
                self.setMessage("Message exceeded the cpu time limit.")
                self.setMessage("This is most likley due to an infnite loop.")
                self.setMessage("Check your for and while loops.")
                self.setMessage(("Sometimes you just put a '>' instead of a '<' or forgot to iterate ex: i += 1."))
                break

            elif codeResult.type == "error":
                self.setMessage("Input: "+ caseInput)
                self.setMessage("Error:")
                self.setMessage(codeResult.output)
                i += 1


            elif codeResult.type == "okay":
                given = codeResult.output

                if given == expected:
                    i = i +1

                else:
                    self.correctFlag = False
                    

                    lenDiff = len(expected) - len(given)

                    tooLong = lenDiff < 0			## the given output is too long
                    tooShort = lenDiff > 0			## the given output is too short

                    if tooLong:
                        tail = len(expected)
                        comparableGiven = given[0:tail] 		## makes given the same length as expected
                        leftOver = given[tail:]					## the rest of given output
                        for line in leftOver:
                            self.setMessage("Expected:  " )
                            self.setMessage("Given:     "+  str(line))

                        self.compare(expected,comparableGiven)
                        i += 1

                    elif tooShort:
                        tail = len(given)
                        comparableExpected = expected[0:tail] 		## makes the expected output the same length as given
                        leftOver = expected[tail:]					## the rest of the expected output

                        self.compare(comparableExpected,given)

                        for line in leftOver:
                            self.setMessage("Expected:  "+ line)
                            self.setMessage("Given:     ")
                            i += 1

                    else:
                        self.compare(expected,given)
                        i += 1













