N,T=map(int,input().split())

arr=[[0]*(N) for _ in range(N)]
dx,dy=[-1,0,1,0],[0,1,0,-1]

string=input()
x,y=N//2,N//2

for i in range(N):
    arr[i]=list(map(int,input().split()))

def in_range(x,y):
    return 0<=x and x<N and 0<=y and y<N

dir_num=0
total=arr[x][y]
for cmd in string:
    if cmd =="L":
        dir_num=(dir_num-1)%4
    elif cmd=="R":
        dir_num=(dir_num+1)%4
    else:
        nx=x+dx[dir_num]
        ny=y+dy[dir_num]
        if in_range(nx,ny):
            x=nx
            y=ny
            total+=arr[x][y]
print(total)