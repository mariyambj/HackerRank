ar=[1,2,3,4,5,6]
k=5
count=0
for i in range(0,len(ar)-1):
    for j in range(i+1,len(ar)):
        if(ar[i]+ar[j])%k==0:
            count+=1
print(count)

