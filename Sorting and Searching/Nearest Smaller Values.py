n=int(input())
l=list(map(int,input().split()))
s=[]
res=[]
for i in range(n):
    while s and l[s[-1]]>=l[i]:
        s.pop()
    if s:
        res.append(s[-1]+1)
    else:
        res.append(0)
    s.append(i)
print(*res)
 
