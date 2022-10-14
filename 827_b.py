x = eval(input())
for i in range(x):
    a = eval(input())
    nums = list(map(int, input().split()))
    nums.sort()
    test = False
    if a == 1:
        print('YES')
        continue
    for j in range(a):
        if nums[j] == nums[j-1]:
            test = True
            break
    if test == False:
        print('YES')
    else:
        print('NO')