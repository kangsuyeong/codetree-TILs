N=int(input())

arr=[[0]*N for _ in range(N)]

for i in range(N):
    arr[i]=list(map(int,input().split()))

max_num=0
for i in range(N):
    for j in range(N-2):
        max_num=max(max_num,arr[i][j]+arr[i][j+1]+arr[i][j+2])

print(max_num)