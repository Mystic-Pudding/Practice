M = int(input())
N = int(input())
def findnotsosu(x):
    if(x==1 or x==0):
        return True
    for i in range(2,x):
        if ((x%i)==0):
            return True
    return False
sosu_array = [] 
for i in range(M,N+1,1):
    result=findnotsosu(i)
    if not result:
        sosu_array.append(i)
if(len(sosu_array)==0):
    print(-1)
else:
    print(sum(sosu_array))
    print(min(sosu_array))