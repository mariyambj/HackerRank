def timeConversion(s):
    # Write your code here
    if s[-2:]=="AM":
        if s[:2]=="12":
            return "00"+s[2:-2]
        else:
            return s[:-2]
    elif s[-2:]=="PM":
        if s[:2]=="12":
            return s[:-2]
        else:
            return (str(int(s[:2])+12)+s[2:-2])
    

s = input()
result = timeConversion(s)
print(result)

'''Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example


Return '12:01:00'.


Return '00:01:00'.

Function Description

Complete the  function with the following parameter(s):

: a time in  hour format
Returns

: the time in  hour format
Input Format

A single string  that represents a time in -hour clock format (i.e.:  or ).

Constraints

All input times are valid
Sample Input 0

07:05:45PM
Sample Output 0

19:05:45'''