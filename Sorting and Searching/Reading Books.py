n = int(input())
arr = list(map(int, input().split()))
 
l = len(arr)
tempMax = 0
sum = 0
 
for i in range(l):
    sum += arr[i]
    tempMax = max(tempMax, arr[i])
 
if(tempMax > sum - tempMax):
    print(2* tempMax)
 
else:
    print(sum)
