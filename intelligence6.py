def threats(n,r):
    sum,sum1=0,0
    while n!=0:
        rem=n%10
        sum=sum+rem
        n=n//10
    total=sum*r
    while total!=0:
        rem=total%10
        sum1+=rem
        total//=10
    return sum1

    
n=int(input("enter the value of 'N'"))
r=int(input("Enter the vslue of 'R"))
print(threats(n,r))
