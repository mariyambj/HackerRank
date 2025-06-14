def total_amount(ages):
    amount = 0
    for age in ages:
        if age < 17:
            amount += 200
        elif 17 <= age < 40:
            amount += 400
        else:
            amount += 300
    return amount

ages = []
while True:
    i = input("Enter the age : ")
    if i == "":
        print("Invalid input")
        break
    age = int(i)
    if age <= 0 or age > 120:
        print("Invalid input")
        continue
    if len(ages) < 20:
        ages.append(age)
    else:
        print("Exceed the limit")
        break

print("Total Amount:", total_amount(ages))


