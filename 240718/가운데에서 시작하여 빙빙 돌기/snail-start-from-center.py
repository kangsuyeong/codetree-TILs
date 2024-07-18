n=int(input())

x,y=n//2,n//2

arr=[[0]*n for _ in range(n)]
dx,dy=[0,-1,0,1],[1,0,-1,0]
dir_num=3
arr[x][y]=1

def in_range(x,y):
    return 0<=x<n and 0<=y<n

for i in range(2,n*n+1):
    dir_num=(dir_num+1)%4
    nx,ny=x+dx[dir_num],y+dy[dir_num]
    if arr[nx][ny]==0:
        x,y=nx,ny
        arr[x][y]=i

    else :
        dir_num=(dir_num-1)%4
        nx,ny=x+dx[dir_num],y+dy[dir_num]
        x,y=nx,ny

        arr[x][y]=i

for row in arr:
    print(*row)