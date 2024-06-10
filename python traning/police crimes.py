def crimes(n, events):
    o = 0
    uc = 0
    
    for e in events:
        if e == -1:
            if o > 0:
                o -= 1
            else:
                uc += 1
        else:
            o += e
    
    return uc

n = int(input())
events = list(map(int, input().split()))
result = crimes(n, events)
print(result)
