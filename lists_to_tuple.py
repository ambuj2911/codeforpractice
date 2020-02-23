

l1 = input()
k = list(l1)
l2 = input()
p = list(l2)

s=[]

def m_tuple():

    try:
        j=0
        for i in range(len(k)):
           s.append((int(k[i]),int(p[j])))
           j=j+1

    except IndexError:
        None

m_tuple()
print(s)