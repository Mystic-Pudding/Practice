S = input()
pikachu = ["pi","ka","chu"]
for x in pikachu:
    S=S.replace(x,"")
if not (len(S)>0):
    print("YES")
else:
    print("NO")