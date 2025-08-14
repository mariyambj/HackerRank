from collections import Counter
b='X_Y__X'
b=list(b)
freq=Counter(b)
for item,count in freq.items():
    if item !='_' and count==1:
        print("No")

print(freq)









    
    