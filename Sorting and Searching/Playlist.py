n= int(input())
a = list(map(int,input().split()))
max_count = 1 
s= set()
i = 0
j = 0
while(j<n):
    if(a[j] in s):
        max_count = max(j-i, max_count)
        count = 1
        while(a[i]!=a[j]):
            s.remove(a[i])
            i+=1
        i+=1
 
    else:
        s.add(a[j])
    j+=1
 
print(max(max_count,j-i))
