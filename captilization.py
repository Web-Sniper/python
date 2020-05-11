#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    f,l = s.split()
    f = list(f)
    l = list(l)
    f[0]=f[0].upper()
    l[0]=l[0].upper()
    f= ''.join(f)
    l=''.join(l)
    s= f+' '+l
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
