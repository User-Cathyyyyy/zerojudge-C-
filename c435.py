import sys

for n in sys.stdin:
    n=int(n)

    ans=0
    data=[int(e) for e in sys.stdin.readline().split()]

    max=data[0]
    for i in range(1, n):
        if data[i]>max:
            max=data[i]
        else:
            temp=max-data[i]
            if temp>ans:
                ans=temp
    print(ans)
