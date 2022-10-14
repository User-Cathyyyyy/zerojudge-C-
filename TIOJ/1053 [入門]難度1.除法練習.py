p, q=input().split()
p=int(p)
q=int(q)
if p>q:
    if p%q==0:
        print('Y')
    else:
        print('N')
else:
    if q%p==0:
        print('Y')
    else:
        print('N')
