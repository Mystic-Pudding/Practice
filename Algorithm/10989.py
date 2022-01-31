N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))
numbers.sort()
for i in range(len(numbers)):
    print(numbers[i])