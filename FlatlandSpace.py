n=5
c=[0,2]
distance=[]
for i in range(0,n):
    min_distance = float('inf')
    for point in c:
        min_distance = min(min_distance, abs(i - point))
    distance.append(min_distance)
print(max(distance))




    #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    c.sort()
    max_distance=c[0]-0
    for i in range(len(c)-1):
        gap=(c[i+1]-c[i])//2
        if gap>max_distance:
            max_distance=gap
    end_gap=(n-1)-c[-1]
    if end_gap>max_distance:
        max_distance=end_gap
    return max_distance
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
