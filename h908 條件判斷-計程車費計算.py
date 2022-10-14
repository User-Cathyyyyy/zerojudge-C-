k, w=input().split()
k=int(k)
w=int(w)
if k>0:
    money1=70+(k-1)*10
else:
    money1=70
money2=(w//3)*5
print(money1+money2)
