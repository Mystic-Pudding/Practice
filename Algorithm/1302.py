# N=int(input())
# solutions={}
# for _ in range(N):
#     data=input()
#     if data in solutions.keys():
#         solutions[data] = solutions[data]+1
#     else:
#         solutions[data] = 1
# if(list(solutions.values()).count(list(solutions.values())[0]) == len(list(solutions.values()))):
#     sortsolutions = list(solutions.keys())
#     sortsolutions.sort()
#     print(sortsolutions[0])
# else:
#     print(max(solutions))
a=[1,2,3]
a.remove(1)
print(a)