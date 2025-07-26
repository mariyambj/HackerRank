arr = [1,6, 7, 7, 8, 10, 12, 13, 14, 19]
d=3
count=0
freq={}
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for num in freq:
    if num+d in freq and num+2*d in freq:
        count+=freq[num]* freq[num+d]*freq[num+2*d]
print(count)


'''Given a sequence of integers , a triplet  is beautiful if:

Given an increasing sequenc of integers and the value of , count the number of beautiful triplets in the sequence.

Example


There are three beautiful triplets, by index: . To test the first triplet,  and .

Function Description

Complete the beautifulTriplets function in the editor below.

beautifulTriplets has the following parameters:

int d: the value to match
int arr[n]: the sequence, sorted ascending
Returns

int: the number of beautiful triplets
Input Format

The first line contains  space-separated integers,  and , the length of the sequence and the beautiful difference.
The second line contains  space-separated integers .

Constraints

Sample Input

STDIN           Function
-----           --------
7 3             arr[] size n = 7, d = 3
1 2 4 5 7 8 10  arr = [1, 2, 4, 5, 7, 8, 10]
Sample Output

3'''