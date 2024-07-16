N,M=map(int,input().split())

arr=[[0]*(N+1) for _ in range(N+1)]

def in_range(x,y):
    return 0<x and x<=N and 0<y and y<=N

dx,dy=[0,1,0,-1],[1,0,-1,0]


for _ in range(M):
    com=0
    r,c=map(int,input().split())
    arr[r][c]=1

    cnt=0
    for i in range(4):
        nx=r+dx[i]
        ny=c+dy[i]
        if in_range(nx,ny) and arr[nx][ny]==1:
            cnt+=1

    if cnt==3:
        com=1
    print(com)