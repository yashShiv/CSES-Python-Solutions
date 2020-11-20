n = int(input())
total = 0
ended = 0
res = list()
re = list()
for i in range(n):
    x,y = map(int,input().split())
    res.append((y,x))
res.sort()
for i in range(n):
    if(res[i][1] >= ended):
        ended = res[i][0]
        total+=1
print(total)
