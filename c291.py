N = int(input())
Nums = list(map(int, input().split()))
walked = [False] * N
ans = 0
for i in range(N):
    if walked[i]:
        continue
    ans += 1
    pointer = Nums[i]
    while pointer != i:
        walked[pointer] = True
        pointer = Nums[pointer]
print(ans)
