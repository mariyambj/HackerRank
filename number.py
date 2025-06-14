n=int(input(("enter the number")))
count=0
for i in range(1,n+1):
	if(i%7==0):
		count+=1
rem=n%7
if ((rem%7)>0 and ((rem%7)<=6)):
	count+=1
print(count)