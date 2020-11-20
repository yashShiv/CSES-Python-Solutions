import bisect
 
x, n = map(int, input().split())
lights = [int(x) for x in input().split()]
 
p = lights[:]
p.append(0)
p.append(x)
p.sort()
 
post = [0] * (n + 1)
for i in range(n + 1):
    post[i] = p[i + 1] - p[i]
back, front = list(range(n + 1)), list(range(n + 1))
 
res = [0] * n
m = max(post)
for i in range(n - 1, -1, -1):
    res[i] = m
    j = bisect.bisect_left(p, lights[i])
    x, y = back[j - 1], front[j]
    post[x] = post[x] + post[j]
    front[x], back[y] = y, x
    
    m = max(m, post[x])
 
print(*res)
