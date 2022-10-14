l=[]
m_num=0
for i in range(10):
    l.append(eval(input()))
for i in range(10):
    if l.count(l[i])>m_num:
        m_num=l.count(l[i])
        M=l[i]
print(M)
print(m_num)