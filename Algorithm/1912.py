n = int(input())
n_array = list(map(int,input().split(' ')))
n_array.sort(reverse=True)
solutions = []
for i in range(n):
    sum = 0
    for k in range(i+1):
        sum = sum + n_array[k]
    solutions.append(sum)
print(max(solutions))
