import IOhandler
import TokenGenerator


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
        diffDetails		=>  a list that contains each line of the diffrence between the given and expected ouptuts, i
                            including errors to be displayed to the student.
        message         => a list that contains each line of a message to be displayed to the student on wheather they got the 
                            problem right and the corresponding token.
        correctFlag		=>  only stays true if the student's code passes each test case.

        """
        self.studentCode = studentCode
        self.studentId = studentId
        self.problemNumber = problemNumber
        self.diffDetails = []
        self.message = []
        self.correctFlag = True

        ###### Setters and Getters######

    def get_StudentId(self):
        """ Returns studentId"""
        return self.studentId

    def get_StudentCode(self):
        """ Returns student code """
        return self.studentCode

    def get_problemNumber(self):
        """Returns problem number."""
        return self.problemNumber

    def get_diffDetails(self):
        """Returns diffDetails"""
        return self.diffDetails

    def set_diffDetails(self,Input):
        if type(Input) == list:
            self.diffDetails.extend(list)
        else:
            self.diffDetails.append(Input)

    def set_message(self):
        T = TokenGenerator.Token(self.studentId,self.correctFlag)
        self.message.extend(T.generateToken())









    def compare(self,expected, given):
        """
        Takes two lists as args, compares the two line by line and appends diffrences
        to self.message to be displayedto the student
        """
        message = self.message
        i = 0
        for line in expected:
            if line != given[i]:
                self.set_diffDetails("Expected: "+str(line))
                self.set_diffDetails("Given:    "+str(given[i]))
                i += 1

    def check(self):
        problem = self.get_problemNumber()
        IO = IOhandler.IO()

        for i in range(IO.getCases(problem)):

            caseNumber = i
            caseInput = IO.getInput(problem, caseNumber)
            expected = IO.getExpected(problem,caseNumber)
            codeResult = IO.OutputHandler(caseInput, self.studentCode,)

            if codeResult.type == "loop":
                self.set_diffDetails("Message exceeded the cpu time limit.")
                self.set_diffDetails("This is most likley due to an infnite loop.")
                self.set_diffDetails("Check your for and while loops.")
                self.set_diffDetails("Sometimes you just put a '>' instead of a '<' or forgot to iterate ex: i += 1.")
                break

            elif codeResult.type == "error":
                self.set_diffDetails("Input: "+ caseInput)
                self.set_diffDetails("Error:")
                self.set_diffDetails(codeResult.output)
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
                            self.set_diffDetails("Expected:  " )
                            self.set_diffDetails("Given:     "+  str(line))

                        self.compare(expected,comparableGiven)
                        i += 1

                    elif tooShort:
                        tail = len(given)
                        comparableExpected = expected[0:tail] 		## makes the expected output the same length as given
                        leftOver = expected[tail:]					## the rest of the expected output

                        self.compare(comparableExpected,given)

                        for line in leftOver:
                            self.set_diffDetails("Expected:  "+ line)
                            self.set_diffDetails("Given:     ")
                            i += 1

                    else:
                        self.compare(expected,given)
                        i += 1
        
        self.set_message()












