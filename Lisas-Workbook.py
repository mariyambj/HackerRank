n=5
k=3
arr=[4,2,6,1,10]
page=1
special=0
for problems in arr:
    for qs in range(1,problems+1):
        if qs==page:
            special+=1
        if qs%k==0:
            page+=1
    if problems % k != 0:
            page += 1
print(special)





    


