def strong_password(length,password):
    numbers='0123456789'
    uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase='abcdefghijklmnopqrstuvwxyz'
    special='!@#$%^&*()-+'
    n=u=l=s=0
    total=0
    
    for i in password:
        if i in numbers:
            n+=1
        if i in uppercase:
            u+=1
        if i in lowercase:
            l+=1
        if i in special:
            s+=1
    if l==0 :
        total+=1
    if s==0:
        total+=1
    if u==0:
        total+=1
    if n==0:
        total+=1
    

    if length<6:
        if 6-length<=total:
            return total
        else:
            return 6-length
    return total

password=input("Enter the password")
n=len(password)
print(strong_password(n,password))