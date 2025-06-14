def price(n):
    product=1
    while n!=0:
        rem=n%10
        product=product*rem
        n=n//10
    return product



n=int(input('Enter the code'))
print(price(n))