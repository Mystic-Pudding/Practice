N = int(input())
A = input().split(' ')
M = int(input())
B = input().split(' ')
answer = []
for i in range(M):
    if B[i] in A:
        answer.append(1)
    else:
        answer.append(0)
for i in answer:
    print(i)