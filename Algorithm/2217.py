N = int(input())
rope = []
for _ in range(N):
  rope.append(int(input()))
rope.sort(reverse = True)

result = []
for i in range(1, N + 1):
  w = i * rope[i-1]
  result.append(w)
print(max(result))