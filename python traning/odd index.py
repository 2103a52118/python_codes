'''dlist= "Hello everyone"
a=dlist[1::2]
print(a)
'''



n=int(input())
nestedlist = [list(map(int,input().split())) for i in range(n)]
print(nestedlist)
maxIn,tsum = 0,0
for index,data in enumerate(nestedlist):
    if tsum< sum(data):
        tsum = sum(data)
        maxIn = index
print(maxIn)
