n= int(input())
a = list(map(int,input().split()))
cost = 0
a.sort()

mid = a[n//2]
for i in a:
    cost+=abs(i-mid)

print(cost)
