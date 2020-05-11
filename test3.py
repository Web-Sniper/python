#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    m = map(str,s.split(' '))
    m = list(m)
    r=[]
    for i in m:
        l=list(i)
        if i.isalpha():
            for j in range(0,len(l)):
                
                if l[j].isalpha():
                    l[j]=l[j].upper()

                    break


        r.append(''.join(l))
    s = ' '.join(r)
    print(m)

    return s

if __name__ == '__main__':
    s = input()

    result = solve(s)

    print(result)

