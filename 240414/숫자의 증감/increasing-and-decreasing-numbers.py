arr=input().split()

c=arr[0]
n=int(arr[1])

if c=='A':
    i=1
    for i in range(1,n+1):
        print(i,end=" ")
elif c=='D':
    i=n
    for i in range(n,1):
        print(i)