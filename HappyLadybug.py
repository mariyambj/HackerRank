from collections import Counter
b='RBY_YBR'
b=list(b)
freq=Counter(b)
bug=False
for item,count in freq.items():
    if item !='_' and count==1:
        bug=True
        break
if '_' in b:
    if bug:
        print("No")
    else:
        print("Yes")
else:
    i=0
    while i <len(b):
        count=1
        while i+1<len(b) and b[i]==b[i+1]:
            i+=1
            count+=1
        if count==1:
            print("No")
        i+=1
    print("yes")










    
    