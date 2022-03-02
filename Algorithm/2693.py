T = int(input())
answer = []
for _ in range(T):
    A = list(map(int,input().split(' ')))
    for _ in range(2):
        remover = max(A)
        A.remove(remover)
    answer.append(max(A))
for ans in answer:
    print(ans)