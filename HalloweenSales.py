def calculate_halloween_sales(p,d,m,s):
    count=0
    cost=p
    while s>=cost:
        s-=cost
        count+=1
        cost=max(cost-d,m)
    return count






p=20
d=3
m=6
s=80
print(calculate_halloween_sales(p,d,m,s))
