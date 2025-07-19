import math
a=3
b=9
count=0
for i in range(a,b+1):
    root=math.sqrt(i)
    if root==int(root):
        count+=1
print(count)

start=math.ceil(math.sqrt(a))
end=math.floor(math.sqrt(b))
print(end-start+1)