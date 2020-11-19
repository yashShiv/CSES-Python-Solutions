n = int(input())
a = set(map(int,input().split())) 
b=set()
c = set()
for i in range(1,n+1):
    b.add(i)
c = b.difference_update(a)
print(*b)
