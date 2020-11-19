t = int(input())
ans = []
 
for i in range(t):
    loc = list(map(int, input().split())) 
 
    if((loc[0]%2)!=0 and (loc[1]%2)==0):
        ans.append((pow(max(loc[0],loc[1])-1, 2))+min(loc[0],loc[1]))
 
    elif(loc[0]%2==0 and loc[1]%2!=0):
        ans.append((pow(max(loc[0], loc[1]), 2)) - min(loc[0], loc[1]) + 1)
 
    elif(loc[0]%2==0 and loc[1]%2==0):
        
        if(loc[0]>loc[1]):
            ans.append(pow(loc[0],2) - loc[1] + 1)
        
        else:
            ans.append(pow(loc[1]-1, 2) + loc[0])
 
    else:
        if(loc[0]>loc[1]):
            ans.append(pow(loc[0]-1, 2) + loc[1])
        else:
            ans.append(pow(loc[1], 2) - loc[0] + 1)
 
for i in ans:
    print(i, end="\n")
