data = input().split(' ')
data = list(map(int,data))
M,N = data[0],data[1]

def find(x):
    if(x==1 or x==0):
        return False
    for i in range(2,x):
        if((x%i)==0):
            return False
    return True
for i in range(M,N+1):
    if(find(i)):
        print(i)
