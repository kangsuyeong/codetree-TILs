# n,m = map(int,input().split())

# answer=[
#     [0 for _ in range(m)]
#     for _ in range(n)
# ]

# grid = [
#     list(map(int,input().split()))
#     for _ in range(n)
# ]

# visited = [
#     [0 for _ in range(m)]
#     for _ in range(n)
# ]


# def in_range(x,y):
#     return 0<=x<n and 0<=y<m

# def can_go(x,y):
#     if not in_range(x,y):
#         return False
#     if visited[x][y] or grid[x][y]==0:
#         return False
    
#     return True

# def dfs(x,y):
#     dxs,dys=[0,1],[1,0]

#     for dx,dy in zip(dxs,dys):
#         new_x,new_y = x+dx, y+dy
#         if can_go(new_x,new_y):
#             answer[new_x][new_y]=1
#             visited[new_x][new_y]=1
#             dfs(new_x,new_y)

# answer[0][0]=1
# visited[0][0]=1
# dfs(0,0)

# if answer[n-1][m-1]==1:
#     print(1)
# else:
#     print(0)



# n,m=map(int,input().split())
# grid = [
#     list(map(int,input().split()))
#     for _ in range(n)
# ]

# visited=[
#     [0 for _ in range(m)]
#     for _ in range(n)
# ]

# def in_range(x,y):
#     return 0<=x<n and 0<=y<m

# def dfs(x,y):
#     visited[x][y]=1
    
#     dxs,dys=[0,1],[1,0]
#     for dx,dy in zip(dxs,dys):
#         nx,ny=x+dx,y+dy
#         if in_range(nx,ny) and grid[nx][ny]==1 and visited[nx][ny]==0:
#             dfs(nx,ny)

# dfs(0,0)
# print(visited[n-1][m-1])


n,m=map(int,input().split())

grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

visited=[
    [0 for _ in range(m)]
    for _ in range(n)
]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def dfs(x,y):
    dxs,dys=[0,1],[1,0]
    for dx,dy in zip(dxs,dys):
        nx,ny=x+dx,y+dy
        if in_range(nx,ny) and grid[nx][ny]==1 and not visited[nx][ny] :
            visited[nx][ny]=1
            dfs(nx,ny)

visited[0][0]=1
dfs(0,0)
print(visited[-1][-1])