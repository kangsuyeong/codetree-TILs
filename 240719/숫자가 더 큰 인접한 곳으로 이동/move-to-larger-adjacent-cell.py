n,r,c=map(int,input().split())
arr=[[0]*(n+1)]

for _ in range(n):
    arr.append([0]+list(map(int,input().split())))



temp=[]

def in_range(x,y):
    return 1<=x<=n and 1<=y<=n

def can_go(x,y,curr_num):
    return in_range(x,y) and arr[x][y]>curr_num


def simulate():
    global r,c
    dxs,dys=[-1,1,0,0],[0,0,-1,1]
    for dx,dy in zip(dxs,dys):
        nx,ny=r+dx,c+dy
        if can_go(nx,ny,arr[r][c]):
            r,c=nx,ny
            return True
    return False
            

temp.append(arr[r][c])

while True:
    greater_number_exist=simulate()

    if not greater_number_exist:
        break;
    temp.append(arr[r][c])

for elem in temp:
    print(elem,end=" ")