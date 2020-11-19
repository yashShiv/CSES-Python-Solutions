a= input()
common = a[0]
maxx=0
count = 0
for i in a:
    if(common==i):
        count += 1
        if(maxx<count):
            maxx = count
    else:
        common = i
        count = 1
print(maxx)
