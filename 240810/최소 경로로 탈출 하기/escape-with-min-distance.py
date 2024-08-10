from collections import deque
n,m=map(int,input().split())

grid = [
    list(map(int,input().split()))
    for _ in range(n)
]
q=deque()

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]
step=[
    [0 for _ in range(m)]
    for _ in range(n)
]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def can_go(x,y):
    return in_range(x,y) and grid[x][y]==1 and not visited[x][y]

def push(x,y,s):
    step[x][y]=s
    visited[x][y] = True
    q.append((x,y))


def bfs():
    while q:
        x,y=q.popleft()
        dxs,dys=[0,1,0,-1],[1,0,-1,0]
        for dx,dy in zip(dxs,dys):
            nx,ny=x+dx,y+dy
            if can_go(nx,ny):
                push(nx,ny,step[x][y]+1)

push(0,0,0)
bfs()
print(step[-1][-1])