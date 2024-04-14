arr=input().split()

a=int(arr[0])
b=int(arr[1])

i=a
while i<=b:
    print(i,end=" ")
    if i%2==1:
        i*=2
    else :
        i+=3