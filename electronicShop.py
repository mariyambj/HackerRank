def getMoneySpent(keyboards, drives, b):
    sums=[]
    for i in keyboards:
        for j in drives:
            sum=i+j
            if sum<=b:
                sums.append(sum)
    #print(sums)
    print(max(sums) if sums else -1)

        
# Given the budget, keyboards, and drives, find the maximum amount of money that can be spent without exceeding the budget.
# If no combination is possible, return -1.

b=10
keyboards=[3,1]
drives=[5,2,8]
getMoneySpent(keyboards, drives, b)