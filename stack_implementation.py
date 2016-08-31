"""
This code is for stack implementation
"""
import re
import sys
#import both sys and regex libraries
def push(number):
    """
    This is our function for the stack push function implementation, it
    doesn't return any value but puts inside a stack called array the
    argument number
    """
    array.append(number)
def pop():
    """
    #This function returns the last element added to a stack.
    """
    return array.pop()

with open(sys.argv[1], 'r') as test_cases:
    #This line opens the file and puts everything into a variable test_cases
    for test in test_cases:
    #This means every line in the file, we iterate over each one of them
        line = test.strip()
        #get our line without spaces at the begining or the end of line.
        toadd = [int(i) for i in re.findall(r"-?\d+", line)]
        #Make a list of integers that we are about to add, so find all numbers positives
        #or negatives from line and add them to toadd.
        array = []
        #Array that will do the stack trick
        final = []
        #List for the values we want, every alternate integer
        for n in toadd:
            push(n)
        #iterate over every number in toadd list and push them into the stack
        for i in range(0, len(array)//2+1):
            #Makes i equal to a value from i = 0 to i = 
            if array != []:
                final.append(str(array.pop()))
                if array != []:
                    array.pop()
                else:
                    break
            else:
                break
        print" ".join(final)
