t = int(input())
res = list()
while(t>0):
    a, b =input().split()
    a, b = int(a), int(b)
 
    if(abs(a-b)<=min(a,b)):
        if((a+b)%3==0):
            res.append("YES")        
        else:
            res.append("NO")
    else:
        res.append("NO")
    t-=1
for i in res:
    print(i, end="\n")
