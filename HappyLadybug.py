from collections import Counter
b='RBY_YBR'
b=list(b)
freq=Counter(b)
if '_' not in b:
    for i in range(len(b)):
        left=(i>0 and b[i]==b[i-1])
        right=(i<len(b)-1 and b[i]==b[i+1])
        if not (left or right):
            print("NO")
    print("YES")
for i in freq:
    if i!='_' and freq[i]==1:
        print("No")
print("YES")











    
    