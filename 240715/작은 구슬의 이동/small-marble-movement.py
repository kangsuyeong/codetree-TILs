n,t=map(int,input().split())
r,c,d=input().split()
r,c=int(r),int(c)

arr=[[0]*(n+1) for _ in range(n+1)]

dxs,dys=[1,0,0,-1],[0,1,-1,0]
mapper={
    'U':2,
    'D':1,
    'R':0,
    'L':3,
}

def in_range(x,y):
    return 0<x and x<=n and 0<y and y<=n

dir_num=mapper[d]

for _ in range(t):
    nx,ny=c+dxs[dir_num],r+dys[dir_num]
    if not in_range(nx,ny):
        dir_num=3-dir_num
    else:
        c+=dxs[dir_num]
        r+=dys[dir_num]

print(r,c)