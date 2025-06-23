#import testwrap
def wrap(string, max_width):
    inilen=0
    for i in range(len(string)) :
        print(string[i],end='')
        inilen+=1
        if inilen==max_width:
            inilen=0
            print('\n',end='')
    return ''
    #return textwrap.fill(string, max_width)

    

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)