def makingAnagrams(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    count = 0
    for ch in s1:
            if ch in s2:
                s2.remove(ch)
            else:
                count += 1
    return count + len(s2)



s1=input("enter the first string:")
s2=input("Enter the second string:")
print(makingAnagrams(s1,s2))