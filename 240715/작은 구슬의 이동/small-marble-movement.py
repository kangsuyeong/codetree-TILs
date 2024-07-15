n,t=map(int,input().split())
r,c,d=input().split()
r,c=int(r),int(c)


dxs,dys=[1,0,0,-1],[0,1,-1,0]
mapper={
    'R':0,
    'U':2,
    'D':1,
    'L':3,
}

def in_range(x,y):
    return 0<x and x<=n and 0<y and y<=n

dir_num=mapper[d]

for _ in range(t):
    nr,nc=r+dys[dir_num],c+dxs[dir_num]
    if not in_range(nc,nr):
        dir_num=3-dir_num
    else:
        r=nr
        c=nc

print(r,c)