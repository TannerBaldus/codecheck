import sys

def multiply(num_half, num_double):
    ## use halving and doubling method to 
    ## find the procut of two numbers
    answer = 0

    while   :
        ##print num_half and num_double at appropriate times (see instructions)
        pass

    

def main():
    stdin = sys.stdin.readline().strip() ##get stdin and clean it up
    numbers = stdin.split() ##create a list by splitting the line

    num_half = int(numbers[0])
    num_double = int(numbers[1])
    multiply(num_half, num_double)

if __name__ == '__main__':
    main()
