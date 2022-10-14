m=eval(input())
for i in range(m):
    num=eval(input())
    tmp=num
    sum_digit=0
    while tmp!=0:
        sum_digit+=tmp%10
        tmp//=10
    print(f'Sum of all digits of {num} is {sum_digit}')
