n,m=map(int,input().split())

arr=[[0]*m for _ in range(n)]

dx,dy=[1,0,-1,0],[0,1,0,-1]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

dir_num=0
cnt=1

x,y=0,0
arr[x][y]=1
for i in range(2,n*m+1):
    nx=x+dx[dir_num]
    ny=y+dy[dir_num]
    if not in_range(nx,ny) or arr[nx][ny]!=0:
        dir_num=(1+dir_num)%4
        nx=x+dx[dir_num]
        ny=y+dy[dir_num]
    x=nx
    y=ny
    arr[x][y]=i

for row in arr:
    print(*row)