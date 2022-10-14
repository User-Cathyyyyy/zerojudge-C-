x, op, y=input().split()#以空格為分隔符
x=eval(x)
y=eval(y)

if op == '+':
    print(x+y)
elif op == '-':
    print(x-y)
elif op == '*':
    print(x*y)
elif op == '/':
    print(x//y)
