
n = int(input())
p = list(map(int, input().split()))
j = [0]*n
for i in range(n):
    k = p[i]
    j[k - 1] = i+ 1
print(" ".join(map(str, j)))

