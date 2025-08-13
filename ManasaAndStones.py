n=2
a=2
b=3
stones=[]
i=0
while i<n:
    if (i+1)-i==a or (i+1)-i==b:
        stones.append(i+1)
    i+=1
print(stones)
    