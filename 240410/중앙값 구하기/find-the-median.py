arr=input().split()

a=int(arr[0])
b=int(arr[1])
c=int(arr[2])

if a>b :
    if b>c:
        print(b)
    else :
        if(a>c):
            print(c)
        else:
            print(a)
else :
    if b<c:
        print(c)
    else :
        if a>c:
            print(a)
        else:
            print(c)