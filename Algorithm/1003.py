def fibonacci(n:int):
    global a
    a=0
    global b
    b=0 
    if n ==0:
        print('0')
        a+=1
        return 0
    elif n==1:
        print('1')
        b+=1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(3))
print(a)
print(b)