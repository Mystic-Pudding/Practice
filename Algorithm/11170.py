T=int(input())
solutions = []
for _ in range(T):
    count = 0 
    nmlist = list(map(int,input().split(' ')))
    N, M = nmlist[0],nmlist[1]
    for i in range(N,M+1,1):
        if '0' in str(i):
            count = count + str(i).count('0')
    solutions.append(count)
for s in solutions:
    print(s)