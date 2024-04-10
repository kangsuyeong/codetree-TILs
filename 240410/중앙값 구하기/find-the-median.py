arr=input().split()

a=int(arr[0])
b=int(arr[1])
c=int(arr[2])

if (a>b and b>c)or(c>b and b>a) :
    print(b)
elif (b>a and a>c) or (c>a and a>b):
    print(a)
else:
    print(c)