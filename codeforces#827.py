x=eval(input())
for i in range(x):
    a, b, c=input().split()
    a=eval(a)
    b=eval(b)
    c=eval(c)
    if a==b+c or b==a+c or c==a+b:
        print('YES')
    else:
        print('NO')
