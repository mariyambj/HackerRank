n=4
m=4
a=[]
for i in range(n):
    for j in range(m):
        print(a[i],a[j],end='\n')
        if i==j:
            a.append(1)
        else:
            a.append(0) 