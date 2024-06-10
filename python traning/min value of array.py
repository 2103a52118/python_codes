t = int(input())
x = 1
while x <= t:
    n, k = map(int, input().split())
    a = [list(map(int, input().split()))for i in range(n-1)]
    mini = 0
    for i in a:
        if i < k:
            mini = max(mini, k - i)
    print(mini)
    x += 1
