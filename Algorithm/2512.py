N = int(input())
numbers = list(map(int,input().split(' ')))
M = int(input())
if(sum(numbers)<=M):
    print(max(numbers))
else:
    under=0
    counter=0
    for n in numbers:
        if(n<=M/N):
           under = under+n 
           counter = counter+1
    print(int((M-under)/(N-counter)))