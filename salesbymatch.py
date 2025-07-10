def sockMerchant(n, ar):
    count=0
    pair={}
    for i in ar:
        if i in pair:
            pair[i]+=1
        else:
            pair[i]=1
    for i in pair:
        count+=pair[i]//2
    return count    



ar=[1,2,1,2,1,3,2]
n=7
print(sockMerchant(n,ar))