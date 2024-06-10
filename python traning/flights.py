T = int(input())
for i in range(T):
    N, p, q, r = map(int, input().split())
    count = 0
    for i in range(1, N + 1):
        tc = (i % p == 0) + (i % q == 0) + (i % r == 0)
        if tc == 1:
            count += 1
    print(count)


