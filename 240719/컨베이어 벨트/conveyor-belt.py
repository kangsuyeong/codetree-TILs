n,t=map(int,input().split())

arr=list(map(int,input().split()))
arr+=list(map(int,input().split()))



for _ in range(t):
    temp=arr[-1]
    arr[1:2*n]=arr[0:2*n-1]
    arr[0]=temp

for i in range(2*n):
    print(arr[i],end=" ")
    if i==n-1:
        print()