t = int(input().strip())
results = []
for _ in range(t):
    n, m = map(int, input().strip().split())
    x1, y1, x2, y2 = map(int, input().strip().split())
    
    if x1 == x2 or y1 == y2:
        results.append(2)
    else:
        if (x1 == 1 or x1 == n) and (x2 == 1 or x2 == n):
            results.append(2)
        elif (y1 == 1 or y1 == m) and (y2 == 1 or y2 == m):
            results.append(2)
        else:
            results.append(3)
for result in results:
    print(result)
