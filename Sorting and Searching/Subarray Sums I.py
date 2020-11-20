from collections import defaultdict
 
n,sum = map(int,input().split())
arr= list(map(int,input().split()))
 
count = 0
sum_history = defaultdict(lambda : 0)
tempSum = 0
 
for i in range(n):
    tempSum += arr[i]
    if tempSum == sum:
        count += 1
    if tempSum - sum in sum_history:
        count += sum_history[tempSum - sum]
        
    sum_history[tempSum] += 1
    
print(count)
