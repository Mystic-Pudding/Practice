n = int(input())
m = int(input())
ab = []
solutions = []
for _ in range(m):
    ab.append(list(map(int,input().split(' '))))

for i in range(m):
    if(ab[i][0]==1):
        solutions.append(ab[i][1])
    if(ab[i][1]==1):
        solutions.append(ab[i][0])
sol=solutions[:]
if (len(sol)>0):
    for s in sol:
        for i in range(m):
            if(s == ab[i][0]):
                if(ab[i][1]!=1):
                    solutions.append(ab[i][1])
            if(s == ab[i][1]):
                if(ab[i][0]!=1):
                     solutions.append(ab[i][0])
print(len(set(solutions)))