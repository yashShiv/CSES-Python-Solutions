n,x = map(int,input().split())
wl = list(map(int,input().split()))
 
c = 0
cp = 1
wl.sort()
i=0
j=n-1
w=wl[j]
while(i<j):
    if(cp==2):
        c+=1
        j-=1
        cp=1
        w=wl[j]
 
    elif(w+ wl[i]>x):
        c+=1
        j-=1
        cp=1
        w = wl[j]
 
    else:
        w+=wl[i]
        i+=1
        cp+=1
print(c+1)
