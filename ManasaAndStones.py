n=3
a=1
b=2
if a>b:
    a,b=b,a
stones=[]
for i in range(n):
    stone=(n-i-1)*b + a*i
    stones.append(stone)
print(stones)    