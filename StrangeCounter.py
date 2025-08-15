import sys

#
# Complete the 'strangeCounter' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER t as parameter.
#

def strangeCounter(t):
    time = 1
    value = 3
    while time + value <= t:
        time += value
        value = 2 * value
    return value - (t - time)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()

    '''There is a strange counter. At the first second, it displays the number . Each second, the number displayed by decrements by  until it reaches . In next second, the timer resets to  and continues counting down. The diagram below shows the counter values for each time  in the 
    first three cycles:https://s3.amazonaws.com/hr-challenge-images/22185/1469447349-bae87a5071-strange1.png
    
    Find and print the value displayed by the counter at time .

Function Description

Complete the strangeCounter function in the editor below.

strangeCounter has the following parameter(s):

int t: an integer
Returns

int: the value displayed at time 
Input Format

A single integer, the value of .'''