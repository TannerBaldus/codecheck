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
            self.diffDetails.extend(Input)
        else:
            self.diffDetails.append(Input)

    def set_message(self):
        T = TokenGenerator.Token(self.studentId,self.correctFlag)
        self.message.extend(T.generateToken())




    def compare(self, expected, given):
        """
        Takes two lists as args, compares the two line by line and appends diffrences
        to self.diffDetails to be displayed to the student
        """
        i = 0
        
        lenDiff = len(expected) - len(given)
        tooLong = lenDiff < 0           ## the given output is too long
        tooShort = lenDiff > 0          ## the given output is too short
        
        if lenDiff == 0:
            for line in expected:
                if line != given[i]:
                    self.set_diffDetails("Expected output:    "+str(line))
                    self.set_diffDetails("Your code's output: "+str(given[i]))
                i += 1

        elif tooLong:
            tail = len(expected)
            comparableGiven = given[0:tail]         ## makes given the same length as expected
            leftOver = given[tail:]
            eofMessage =["End of ouput" for i in range(len(leftOver))]
            compare(expected, comparableGiven)
            compare(eofMessage,leftOver)

            
        elif tooShort:
            tail = len(given)
            comparableExpected = expected[0:tail]       ## makes the expected output the same length as given
            leftOver = expected[tail:]
            eofMessage = ["End of output" for i in range(len(leftOver))]
            compare(comparableExpected,given)
            compare(leftover, eofMessage)










        



    def check(self):
        problem = self.get_problemNumber()
        IO = IOhandler.IO()

        for i in range(IO.getCases(problem)):

            caseNumber = i
            caseInput = IO.getInput(problem, caseNumber)
            self.set_diffDetails("---------------------------------------------")
            self.set_diffDetails("Input: "+str(caseInput))
            self.set_diffDetails("---------------------------------------------")
            expected = IO.getExpected(problem,caseNumber)
            codeResult = IO.OutputHandler(caseInput, self.studentCode,)

            if codeResult.type == "loop":
		self.correctFlag = False
                self.set_diffDetails("Message exceeded the cpu time limit.")
                self.set_diffDetails("This is most likley due to an infnite loop.")
                self.set_diffDetails("Check your for and while loops.")
                self.set_diffDetails("Sometimes you just put a '>' instead of a '<' or forgot to iterate ex: i += 1.")
                break

            elif codeResult.type == "error":
		self.correctFlag = False
                self.set_diffDetails("Your code produced an error:")
                self.set_diffDetails(codeResult.output)
                i += 1


            elif codeResult.type == "okay":
                given = codeResult.output

                if given == expected:
                    for j in range(len(expected)):
                        self.set_diffDetails("Expected output: "+str(expected[j]))
                        self.set_diffDetails("Your code's output:    "+str(given[j]))
                    i += 1
                

                else:
                    self.correctFlag = False
                    self.compare(expected,given)
                    i += 1

                   

                   
        
        self.set_message()












