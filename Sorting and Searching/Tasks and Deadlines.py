n = int(input())
arr = []
for i in range(n):
    a, d = map(int, input().split())
    arr.append((a,d))
 
arr.sort()
reward = 0
duration = 0
 
for i in range(n):
    duration += arr[i][0]
    reward += arr[i][1] - duration
    
 
print(reward)
