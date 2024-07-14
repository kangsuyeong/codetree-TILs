n=int(input())

arr=[[0]*n for _ in range(n)]
dxs,dys=[1,0,-1,0],[0,-1,0,1]

for i in range(n):
    arr[i] = list(map(int,input().split()))

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

total=0
cnt=0
for i in range(n):
    for j in range(n):
        #4번 돌아라
        for dx,dy in zip(dxs,dys):
            x,y=i+dx,j+dy
            if in_range(x,y) and arr[x][y]==1:
                cnt+=1
        if cnt>=3:
            total+=1
        cnt=0

print(total)