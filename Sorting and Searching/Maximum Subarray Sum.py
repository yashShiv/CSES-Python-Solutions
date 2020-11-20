n= int(input())
a = list(map(int,input().split()))
 
t = 0
p = -1e9
for i in range(n):
    t += a[i]
    if(p < t):
        p = t
 
    if(t<0):
        t = 0
 
print(p)
