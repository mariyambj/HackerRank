#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    n=len(container)
    container_sum=[]
    for i in range(n):
        row_sum=0
        for j in range(n):
            row_sum+=container[i][j]
        container_sum.append(row_sum)
    type_sum=[]
    for j in range(n):
        column_sum=0
        for i in range(n):
            column_sum+=container[i][j]
        type_sum.append(column_sum)
    container_sum.sort()
    type_sum.sort()
    if container_sum==type_sum:
        result="Possible"
    else:
        result= "Impossible"
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
