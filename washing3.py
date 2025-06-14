def total_min(weight):
    min = 0
    if weight ==0:
        print("invalid input")
    elif weight>0 and weight<=2000:
        min=25
    elif weight >=2001 and weight <=4000:
        min= 35
    elif weight >4000 and weight<=7000:
        min=45
    else:
        print("overloaded")
    return (min)
weight=int(input("enter the weightof the clothes:"))
print(total_min(weight),"minutes")