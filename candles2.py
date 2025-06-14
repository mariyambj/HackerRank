n=int(input("enter the maximum capacity of jar"))
k=int(input("Enter the minimum candles should be in the jar"))
i=int(input("enter the number of candles:"))
if i == 0:
    print("invalid input")
elif(i<=k):
    print("NUMBER OF CANDIES SOLD : ",i)
    print("NUMBER OF CANDIES LEFT :",n-i)
elif i>k:
    print("No sufficient candles")
    print("NUMBER OF CANDIES LEFT :",n)

