s = input()
first = ""
second = ""
res1 = set()
odd = False
count = 0
for i in s:
    res1.add(i)
 
for i in res1:
    x = s.count(i)
  
 
    if(x & 1):
        count+=1
        oddc = i
        oddcount = x
        odd = True
    
 
if(odd):
    s = s.replace(oddc,'', oddcount)
    oddc = oddc*oddcount
 
if(count>1):
    print("NO SOLUTION")
 
else:
    s = sorted(s)
    y = -1
    j = 0
    for i in range(len(s)):
        if(i & 1):
            second = second + s[i]
        else:
            first = first + s[i]
 
    second = second[::-1]
 
    if(odd):
        print(first + oddc + second)
 
    else:
        print(first + second)
