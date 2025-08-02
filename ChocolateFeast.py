n=15
c=3
m=2
chocolate=n//c
wrapper=chocolate
while wrapper>=m:
    extra=wrapper//m
    chocolate+=extra
    wrapper=wrapper%m+extra
print(chocolate)