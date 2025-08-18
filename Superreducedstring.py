def super_reduced_string(s):
    stack=[]
    for char in s:
        if stack and stack[-1]==char:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

string="aaabccddd"
print(super_reduced_string(string))