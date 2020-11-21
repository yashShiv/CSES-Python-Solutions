n = int(input())

for i in range(1,n+1):
    total = i**2*(i**2 - 1)//2
    vulnerable = 4 * (i-1) * (i-2)
    res = total - vulnerable
    print(res)
