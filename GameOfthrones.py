def gameOfThrones(s):
    char = []
    for i in s:
        if i not in char:
            char.append(i)
        else:
            char.remove(i)
    
    if len(char) <= 1:
        return "YES"
    else:
        return "NO"

s = input("Enter the string: ")
print(gameOfThrones(s))


