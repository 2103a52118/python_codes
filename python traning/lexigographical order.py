"""d=int(input())
rlist=[str(i) for i in range(1,d+1)]
rlist.sort()
print(list(map(int,rlist)))"""


'''dlist= input("input:").split()
if len(dlist) > 1:
    first, *middle, last = dlist
    dlist = [last, *middle, first]
elif len(dlist) == 1:
        dlist= dlsit
print(dlist)'''


house=list(map(int,input().split()))
emax=sum(house[0::2])
omax=sum(house[1::2])
tmax=0
while(max(house)!=0):
    tmax+=max(house)
    i=house.index(max(house))
    if i==0:
        house[0],house[1]=0,0
    elif i == len(house)-1:
        house[-2],house[-1]=0,0
    else:
        house[i],house[i+1],house[i-1]=0,0,0
print(max([omax,emax,tmax]))
