def oddEven(n):
    if(n & 1)==0:
        return "Even"
    else:
        return"Odd"




n=int(input("Enter the number n"))
print(oddEven(n))