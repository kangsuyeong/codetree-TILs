import sys
N=int(input())

arr=[
    list(map(int,input().split()))
    for _ in range(N)
]

min_num=sys.maxsize
# i 체크포인트
for i in range(1,N-1):
    pre=0
    dist=0
    for j in range(N):
        if i==j:
            continue
        dist+=abs(arr[pre][0]-arr[j][0])+abs(arr[pre][1]-arr[j][1])
        pre=j
    min_num=min(min_num,dist)
print(min_num)