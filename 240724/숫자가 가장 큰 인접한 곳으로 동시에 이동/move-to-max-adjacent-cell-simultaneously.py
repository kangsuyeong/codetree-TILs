n,m,t=map(int,input().split())

arr=[[0]*(n+1)]
for _ in range(n):
    arr.append([0]+list(map(int,input().split())))

Count = [[0]*(n+1)
    for _ in range(n+1)
]
new_Count = [
    [0]*(n+1)
    for _ in range(n+1)
]
# 카운트에 채우기
for _ in range(m):
    r,c=map(int,input().split())
    Count[r][c]=1

# dx,dy
dxs,dys=[-1,1,0,0],[0,0,-1,1]

def in_range(x,y):
    return 0<x<=n and 0<y<=n

def simulate():
    for i in range(1,n+1):
        for j in range(1,n+1):
            new_Count[i][j]=0

    global Count,arr
    for i in range(1,n+1):
        for j in range(1,n+1):
            if Count[i][j]==1:
                max_num=0
                max_x,max_y=0,0
                for dx,dy in zip(dxs,dys):
                    nx,ny=i+dx,j+dy
                    if in_range(nx,ny) and max_num<arr[nx][ny]:
                        max_num=arr[nx][ny]
                        max_x,max_y=nx,ny
                new_Count[max_x][max_y]=1           
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            Count[i][j]=new_Count[i][j]


def remove_dup():
    for i in range(1,n+1):
        for j in range(1,n+1):
            if Count[i][j]>=2:
                Count[i][j]=0

for _ in range(t):
    simulate()
    remove_dup()


s=0

for row in Count:
    s+=sum(row)
print(s)