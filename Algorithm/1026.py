N = int(input())
A_array = input().split(' ')
A_array = list(map(int,A_array))
B_array = input().split(' ')
B_array = list(map(int,B_array))
A_array.sort()
def S(A,B):
    sum = 0
    for i in range(N):
        sum = sum + (A[i]*B[i])
    return sum
corrects = [] 
for i in range(N):
    correct = max(B_array)
    corrects.append(correct)
    B_array.remove(correct)
result = S(A_array,corrects)
print(result)