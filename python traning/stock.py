a=list(map(int,input().split()))
h=[]
for i in range(len(a)):
    x=min(a)
    m = a.index(x)
    if m+1==len(a):
        a.remove(x)
        l=a[:m]
        x1=min(l)
        y=max(l)
        n=l.index(y)+m  
    else:
        l=a[m:]
        x1=x
        y=max(l)
        n=l.index(y)+m
    if m<n :
        h.append(y-x1)
    else:
        print(0)
print(h)
t=max(h)
print(t)
