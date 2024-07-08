N=int(input())

arr=list(map(int,input().split()))
arr.sort()


max_num = arr[0] + arr[2*N-1]
for i in range(1,N):
    if max_num < arr[i] + arr[2*N-1-i]:
        max_num = arr[i] + arr[2*N-1-i]
print(max_num)