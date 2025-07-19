#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    count_stick=[]
    while arr:
        count_stick.append(len(arr))
        cur_min=min(arr)
        #print(cur_min)
        new_arr=[]
        for i in arr:
            if i >cur_min:
                new_arr.append(i-cur_min)
        arr=new_arr
    return count_stick

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
