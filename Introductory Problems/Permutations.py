a = int(input())
if(a==1):
    print(1)
 
elif(a<=3 and a>1):
    print("NO SOLUTION")
    
else:
    for j in range(2,a+1,2):
        print(j, end =" ")
    for i in range(1,a+1,2):
        print(i, end =" ")
 
