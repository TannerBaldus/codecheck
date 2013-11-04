import sys
def compare(expected, given):
        """
        Takes two lists as args, compares the two line by line and appends diffrences
        to self.message to be displayedto the student
        """
        i = 0
        
        lenDiff = len(expected) - len(given)
        tooLong = lenDiff < 0           ## the given output is too long
        tooShort = lenDiff > 0          ## the given output is too short
        
        if lenDiff == 0:
            for line in expected:
                if line != given[i]:
                    print("Expected output:    "+str(line))
                    print("Your code's output: "+str(given[i]))
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
            compare(leftOver, eofMessage,)


x = [1,2,3]
y =[1,2,3,4,5,6,7]
compare(y,x)