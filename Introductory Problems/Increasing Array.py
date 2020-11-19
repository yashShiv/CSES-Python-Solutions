n = int(input())
a = list(map(int,input().split())) 
t = 0
for i in range(1,len(a)):
    if(a[i-1]>a[i]):
        t=t+(a[i-1]-a[i])
        a[i]=a[i-1]
print(t)
