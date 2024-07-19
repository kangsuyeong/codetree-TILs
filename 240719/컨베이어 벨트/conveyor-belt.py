n,t=map(int,input().split())

arr=list(map(int,input().split()))
arr+=list(map(int,input().split()))



for _ in range(t):
    temp=arr[len(arr)-1]
    for i in range(n*2-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=temp

for i in range(2*n):
    print(arr[i],end=" ")
    if i==n-1:
        print()