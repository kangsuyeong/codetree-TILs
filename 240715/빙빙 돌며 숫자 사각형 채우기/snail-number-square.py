n,m=map(int,input().split())

ans=[[0]*m for _ in range(n)]

r,c=0,0
drs,dcs=[0,1,0,-1],[1,0,-1,0]
dir_num=0

def in_range(r,c):
    return 0<=r and r<n and 0<=c and c<m

ans[r][c]=1

for i in range(2,n*m+1):
    nr,nc=r+drs[dir_num],c+dcs[dir_num]
    if not in_range(nr,nc) or ans[nr][nc]!=0:
        dir_num=(dir_num+1)%4
    r,c=r+drs[dir_num],c+dcs[dir_num]
    ans[r][c]=i

for row in ans:
    for elem in row:
        print(elem,end=" ")
    print()