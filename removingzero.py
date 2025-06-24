'''a=[1,0,0,3,0,4]
b=[]
c=[]
for i in a:
    if i==0:
        b.append(i)
    else:
        c.append(i)
print(c+b)'''

a=[1,0,0,3,0,4,0]
i=0
j=0
while j<len(a):
    if a[j]!=0:
        a[i],a[j]=a[j],a[i]
        i+=1
    j+=1
print(a)
