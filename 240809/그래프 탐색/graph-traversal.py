N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
cnt=0

for _ in range(M):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(vertex):
    global cnt
    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            cnt+=1
            visited[curr_v]=True
            dfs(curr_v)

root_vertex=1
visited[root_vertex]=True
dfs(root_vertex)
print(cnt)