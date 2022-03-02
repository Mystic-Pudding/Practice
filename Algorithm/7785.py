from audioop import reverse


n = int(input())
enter = {}
solution = []
for _ in range(n):
    candidate = input().split(" ")
    enter[candidate[0]] = candidate[1]
for key in enter.keys():
    if(enter[key] == "enter"):
        solution.append(key)
    else:
        pass
solution.sort(reverse=True)
for s in solution:
    print(s)