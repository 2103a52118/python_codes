'''
n=input("enter string:")
result = ""
pre = None
for char in n:
  if char != pre:
    result += char
  pre = char
print(result)

*******************************
data=input()
rot=int(input())
res=''
for i in range(rot):
  di,mag=input().split()
  if di.upper=='L':
    (data[mag:]+data[:int(mag)])
  elif di.upper()=="R":
    res+=(data[:int(mag)]+data[int(mag)])
subList=[data[i:i+rot] for i in range(len(data))]
for subele in subList:
  if sorted(subele)==sorted(res):
    print("Yes")
    break
else:
    print("No")

****************************'''
from collections import deque


data = input().strip()
qstr = deque(input().strip())
rot = int(input().strip())
res = ''


for i in range(rot):
    di, mag = input().split()
    mag = int(mag)
    if di.lower() == 'l':
        qstr.rotate(-mag)  
    elif di.lower() == 'r':
        qstr.rotate(mag)  
    res += qstr[0]


subList = [data[i:i+rot] for i in range(len(data)-rot+1)]


for suble in subList:
    if sorted(suble) == sorted(res):
        print("yes")
        break
else:
    print("no")


