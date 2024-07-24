n,r,c=map(int,input().split())
arr=[[0]*(n+1)]

for _ in range(n):
    arr.append([0]+list(map(int,input().split())))



# 범위 안에 있는지 확인하는 함수
def in_range(x,y):
    return 0<x<=n and 0<y<=n
temp=[]

# 움직이는 함수
def move(x,y,current_num):
    global r,c
    next_pos=(0,0)
    # dx ,dy
    dxs,dys=[-1,1,0,0],[0,0,-1,1]
    for dx,dy in zip(dxs,dys):
        nx,ny=x+dx,y+dy
        if in_range(nx,ny) and arr[nx][ny]>current_num:
            r,c=nx,ny
            temp.append(arr[nx][ny])
            return True 
    return False


# 실행
# 첫번째 칸 추가
temp.append(arr[r][c])

while True:
    if not move(r,c,arr[r][c]):
        break;

for elem in temp:
    print(elem,end=" ")