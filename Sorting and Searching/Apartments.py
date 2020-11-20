n,m,k = map(int,input().split())
des = list(map(int,input().split()))
avl = list(map(int,input().split()))
 
des.sort()
avl.sort()
 
cnt = 0
i = 0
j = 0
while(i<n and j<m):
    if(abs(des[i] - avl[j]) <=k):
        cnt+=1
        i+=1
        j+=1
        
    elif(des[i]< avl[j]):
        i+=1
 
    elif(des[i]>=avl[j]):
        j+=1
 
print(cnt)
