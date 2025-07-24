#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    a=[]
    if p>q :
        return "INVALID RANGE"
    for n in range(p, q + 1):
        square = str(n ** 2)
        r = len(str(n))
        right = int(square[-r:]) if square[-r:] else 0
        left = int(square[:-r] or 0)
        if left + right == n :
            a.append(str(n))
    if not a:
        print("INVALID RANGE")
    else:
        print(' '.join(a))


if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)


