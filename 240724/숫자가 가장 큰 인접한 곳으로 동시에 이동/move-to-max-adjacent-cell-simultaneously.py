n,m,t=map(int,input().split())

# 기존배열
arr=[[0]*(n+1)]
for _ in range(n):
    arr.append([0]+list(map(int,input().split())))
# 위치배열
count = [
    [0]*(n+1)
    for _ in range(n+1)
]

for _ in range(m):
    r,c=map(int,input().split())
    count[r][c]=1

# 위치 이동배열
next_count=[
    [0]*(n+1)
    for _ in range(n+1)
]

def in_range(x,y):
    return 0<x<=n and 0<y<=n


# 위치 이동시키기

def move():
    dxs,dys=[-1,1,0,0],[0,0,-1,1]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if count[i][j]==1:
                max_num=0
                max_x,max_y=0,0
                for dx,dy in zip(dxs,dys):
                    nx,ny=i+dx,j+dy
                    if in_range(nx,ny) and max_num<arr[nx][ny]:
                        max_num=arr[nx][ny]
                        max_x,max_y=nx,ny

                next_count[max_x][max_y]+=1

def remove_dup():
    for i in range(1,n+1):
        for j in range(1,n+1):
            if next_count[i][j]>=2:
                next_count[i][j]=0




for _ in range(t):
    move()
    remove_dup()
    # 복사
    for i in range(1,n+1):
        for j in range(1,n+1):
            count[i][j]=next_count[i][j]
    # 초기화
    for i in range(1,n+1):
        for j in range(1,n+1):
            next_count[i][j]=0

# 최종결과
s=0
for elem in count:
    s+=sum(elem)
print(s)