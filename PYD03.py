a=int(input())
b=int(input())
sum=0
for n in range(a, b+1):
    if n%2==0:
        sum+=n
print(sum)
