K = int(input())
answer = []
for i in range(0,K):
    x = int(input())
    if (x==0):
        del answer[-1:]
    else:
        answer.append(x)
print(sum(answer))