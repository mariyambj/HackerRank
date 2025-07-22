#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    n=len(s)
    encrypted=[]
    c=math.floor(math.sqrt(n))
    f=math.ceil(math.sqrt(n))
    if c*f<n:
        c+=1
    for col in range(f):
        word=""
        for row in range(c):
            index=row*f+col
            if index<n:
                word+=s[index]
        encrypted.append(word)
    return " ".join(encrypted)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
