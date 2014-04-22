import IOhandler
import TokenGenerator


class Checker(object):
    """
    Summary
    -------
    Implements compare and check methods to grade check the student's output
    against the expected output of multiple test cases.


    Methods
    --------
    __init__
    compare
    check
    getters for :
        studentId
        studentCode
        problemNumber
        diffDetails
    setters for:
        diffDetails
        message


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
        """ Adds token to message"""
        T = TokenGenerator.Token(self.studentId,self.correctFlag)
        self.message.extend(T.generateToken())




    def compare(self, expected, given):
        """
        Takes two lists as args, compares the two line by line and appends diffrences
        to self.diffDetails to be displayed to the student

        If the given output is too long, Splits the given output into:
        comparableGiven: the same length as expected 
        leftover: the rest of given output
        it then calls comparae on expected andcomparableGiven
        and then compare on and end of file message(the same length) as leftover.

        And vice versa when given is too short.


        """
        i = 0
        
        lenDiff = len(expected) - len(given)
        tooLong = lenDiff < 0           ## the given output is too long
        tooShort = lenDiff > 0          ## the given output is too short
        
        if lenDiff == 0:
            for line in expected:
                if line != given[i]:
                    self.set_diffDetails("Expected output:    "+str(line)) ##add
                    self.set_diffDetails("Your code's output: "+str(given[i]))
                i += 1

        elif tooLong:
            tail = len(expected)
            comparableGiven = given[0:tail]         ## makes comparableGiven the same length as expected
            leftOver = given[tail:]
            eofMessage =["End of ouput" for i in range(len(leftOver))] ##create EOF message the size of leftover
            self.compare(expected, comparableGiven)
            self.compare(eofMessage,leftOver)

            
        elif tooShort:
            tail = len(given)
            comparableExpected = expected[0:tail]       ## makes the comparableExpected output the same length as given
            leftOver = expected[tail:]
            eofMessage = ["End of output" for i in range(len(leftOver))]
            self.compare(comparableExpected,given)
            self.compare(leftOver, eofMessage)










        



    def check(self):
        """
        The main function of the Checker class. Uses IOHandler to run the students code and appends the appropriate content
        into diffDetails for all test cases of the problem. If the students code does not produces and error but produces incorrect output uses compare 
        to add the diffence between outputs to diffDetails. In the case of an error it appends the error message to diffDetails.
        if the student's code passes the test cases it appends the full output to diffDetails. 

        """
        problem = self.get_problemNumber()
        IO = IOhandler.IO()

        for i in range(IO.getCases(problem)):

            caseNumber = i
            caseInput = IO.getInput(problem, caseNumber)
            self.set_diffDetails("---------------------------------------------") ##seperators
            self.set_diffDetails("Input: "+str(caseInput))
            self.set_diffDetails("---------------------------------------------") ## seperators
            expected = IO.getExpected(problem,caseNumber)
            codeResult = IO.OutputHandler(caseInput, self.studentCode,)

            if codeResult.type == "loop": ## if the student's code produces a loop
                self.correctFlag = False
                self.set_diffDetails("Message exceeded the cpu time limit.")        ##give special infinite loop message
                self.set_diffDetails("This is most likley due to an infnite loop.")
                self.set_diffDetails("Check your for and while loops.")
                self.set_diffDetails("Sometimes you just put a '>' instead of a '<' or forgot to iterate ex: i += 1.")
                break

            elif codeResult.type == "error": ## if the code produces an error
                self.correctFlag = False
                self.set_diffDetails("Your code produced an error:") 
                self.set_diffDetails(codeResult.output) ## put stderr into diffDetails
                i += 1


            elif codeResult.type == "okay": ##
                given = codeResult.output

                if given == expected: ## if the student's output is correct
                    for j in range(len(expected)):
                        ##show them the outputs
                        self.set_diffDetails("Expected output: "+str(expected[j]))
                        self.set_diffDetails("Your code's output:    "+str(given[j]))
                    i += 1
                

                else:
                    ##the student's output isn't correct
                    self.correctFlag = False
                    self.compare(expected,given) ##compare the given vs expected.
                    i += 1

                   

                   
        
        self.set_message() ## add token to message with teh final value of correctFlag











