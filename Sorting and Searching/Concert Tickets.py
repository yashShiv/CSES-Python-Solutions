import bisect
 
n,m = map(int,input().split())
t = list(map(int,input().split()))
p = list(map(int,input().split()))
 
t.sort()
 
 
for i in p:
    if(len(t)!=0):
        ind = bisect.bisect_left(t,i)
        if(ind == 0 and t[ind] != i):
            print(-1)
            
        else:
            if(ind<len(t) and t[ind] == i):
                print(t[ind])
                del t[ind]
            else:
                print(t[ind -1])
                del t[ind-1]
 
 
    else:
        print(-1)
