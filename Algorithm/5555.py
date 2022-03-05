target = str(input())
N = int(input())
count = 0
for _ in range(N):
    ring = str(input())
    if target in ring:
        count = count+1
        continue
    reversering = ring + ring
    if target in reversering:
        count = count+1
print(count)