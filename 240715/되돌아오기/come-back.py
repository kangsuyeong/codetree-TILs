N=int(input())
OFFSET=1000
mapper={
    'E':0,
    'S':1,
    'W':2,
    'N':3
}

dx,dy=[1,0,-1,0],[0,-1,0,1]

x,y=OFFSET,OFFSET

cnt=0
for i in range(N):
    s,d=input().split()
    d=int(d)
    dir_num=mapper[s]
    for _ in range(d):
        x+=dx[dir_num]
        y+=dy[dir_num]
        cnt+=1
        if x==OFFSET and y==OFFSET:
            break;
    if x==OFFSET and y==OFFSET:
        print(cnt)
        break;
    if i==N-1:
        print(-1)