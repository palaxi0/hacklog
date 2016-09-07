""" Program to get the longest repeated substring """
import sys
with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        line = test.strip()
        substrings = []
        for i in range(0,len(line)):
            for j in range(i+1,len(line)):
                if line[i:j+1].strip() not in substrings and line.count(line[i:j+1].strip())> 1:
                    if line[i:j+1].strip() != "":
                        substrings.append(line[i:j+1].strip())
        if len(substrings) > 0:
            print max(substrings,key=len)
        else:
            print "NONE"
