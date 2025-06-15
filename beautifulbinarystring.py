def BeautifulBinaryString(s):
    sub='010'
    no=s.count(sub)
    return no
    '''count=0
    for i in range(0,s,3):
        if i==0 and i+1==1 and i+2==0:
            count+=1
            continue
    return count'''


n=int(input("enter the length of the string"))
s=int(input("enter the string:"))
print(BeautifulBinaryString(s))