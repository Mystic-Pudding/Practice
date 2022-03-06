N=int(input())
P = list(map(int,input().split(' ')))
P.sort()
hap = 0
solutions = []
for p in P:
    hap = hap + p
    solutions.append(hap)
print(sum(solutions))