string=input()
x,y=0,0
dir_num=0
dx,dy=[0,1,0,-1],[1,0,-1,0]


def move(cmd):
    global dir_num
    global x,y
    if cmd == "L":
        dir_num=(dir_num-1)%4
    elif cmd=="R":
        dir_num=(dir_num+1)%4
    else:
        x+=dx[dir_num]
        y+=dy[dir_num]

ans=0
for cmd in string:
    move(cmd)
    ans+=1
    if x==0 and y==0:
        break;
print(ans)