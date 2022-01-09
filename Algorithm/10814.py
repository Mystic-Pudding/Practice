N = int(input())
array = []
x_array=[]
for i in range(N):
    info = input().split(' ')
    info[0] = int(info[0])
    x_array.append(int(info[0]))
    array.append(info)
x_array.sort()
solutions = []
for i in range(len(x_array)):
    for k in range(len(array)):
        if x_array[i] in array[k]:
            solutions.append(array[k])
            array.remove(array[k])
            break
for i in range(N):
    print("%d %s"%(int(solutions[i][0]),solutions[i][1]))
