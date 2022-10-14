n=int(input())
sum=0
for i in range(n):
    a, b=input().split()
    a=int(a)
    b=int(b)
    for j in range(a, b+1, 1):
        if (j%3==0 or j%4==0) and j%5!=0:
            sum+=j
    print(sum)
    sum=0
            
