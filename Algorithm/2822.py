ques = []
for _ in range(8):
    ques.append(int(input()))
sumlist=[]
maxindexlist = []
for _ in range(5):
    remover = max(ques)
    maxindexlist.append(ques.index(remover)+1)
    sumlist.append(remover)
    ques[ques.index(remover)] = 0
print(sum(sumlist))
maxindexlist.sort()
for m in maxindexlist:
    print(m,"",end="")