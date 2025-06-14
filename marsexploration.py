def marsExploration(s):
    if len(s)% 3!=0:
        return -1
    else:
        count=0
        for i in range(0,len(s),3):
            if s[i]!='S':
                count+=1
            if s[i+1]!='O':
                count+=1
            if s[i+2]!='S':
                count+=1
        return count
            
s=str(input("enter the string message")).upper()
result=marsExploration(s)
print(result)