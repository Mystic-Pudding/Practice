size_a,size_b = input().split(' ')
a = list(map(int,input().split(' ')))
b = list(map(int,input().split(' ')))
solution = a+b
solution.sort()
for k in solution:
    print(str(k) + " ",end="")