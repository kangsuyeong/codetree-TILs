n,m = map(int,input().split())

arr = [[0]*m for _ in range(n)]

dx,dy=[0,1,0,-1],[1,0,-1,0]
dir_num=0

def in_range(x,y):
    return 0<=x<n and 0<=y<m

arr[0][0]='A'
x,y=0,0
for i in range(2,n*m+1):
    nx,ny=x+dx[dir_num],y+dy[dir_num]
    if not in_range(nx,ny) or arr[nx][ny]!=0:
        dir_num=(dir_num+1)%4
        nx,ny=x+dx[dir_num],y+dy[dir_num]
    x,y=nx,ny
    arr[x][y]=chr(ord('A')+(ord('A')+i-1)%65)
    
for row in arr:
    print(*row)