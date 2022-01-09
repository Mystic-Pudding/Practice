def factorial(x):
    fac = 1
    for i in range(x,0,-1): 
        fac = fac*i
    return fac
N = int(input())
count = 1
string = str(factorial(N))[::-1]
if '0' in string : 
    index = string.find('0')
    while(string[index+1]=='0'):
        index = index + 1
        count = count + 1
    print(count)
else:
    print(0)