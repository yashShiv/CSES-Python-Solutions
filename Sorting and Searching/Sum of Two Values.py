n,x = map(int,input().split())
arr = list(map(int, input().split()))
 
if(n>1):
    res = list()
    for i,y in enumerate(arr):
        res.append((y,i+1))
 
    res.sort()
    j=n - 1
    lg = res[j][0]
    i=0
    while(i<j):
        if(res[i][0]+res[j][0] == x):
            print(res[i][1], res[j][1])
            break
 
        elif(res[i][0]+res[j][0] < x):
            i+=1
            continue
 
        elif(res[i][0]+res[j][0] > x):
            j-=1
            continue
    
    if(i==j):
        print("IMPOSSIBLE")
 
else:
    print("IMPOSSIBLE")
