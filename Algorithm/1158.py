data = input().split(' ')
N,K = int(data[0]),int(data[1])
yosefuse = list(range(1,N+1))
count = 0
answer = []
while len(yosefuse):
    for i in range(K-1):
        count = count + 1
    if count>= len(yosefuse):
        count = count%len(yosefuse)
    answer.append(yosefuse[count])
    yosefuse.remove(yosefuse[count])


print('<',end='')
for i in range(len(answer)-1):
    print(answer[i],end=', ')
print(answer[-1],'>',sep='') 
