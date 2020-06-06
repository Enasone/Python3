n=int(input())
ishodnoe=str(input())
konechnoe=str(input())
count_vniz=int()
count_verh=int()
a=list()
b=list()
final=list()
for i in range(n):
    x=int(ishodnoe[i])
    y=int(konechnoe[i])
    while x%10!=y%10:
        x-=1
        count_vniz+=1
        if x<0:
            x=9
    a.append(count_vniz)
    count_vniz=0
    x=int(ishodnoe[i])
    while x%10!=y%10:
        x+=1
        count_verh+=1
    b.append(count_verh)
    count_verh=0
print(a,b)
for i in range(n):
    if a[i]<b[i]:
        final.append(a[i])
    elif b[i]<a[i]:
        final.append(b[i])
print(final)