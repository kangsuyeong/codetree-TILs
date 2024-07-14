x,y=0,0
dx=[0,1,0,-1]
dy=[1,0,-1,0]
dir_num=0

S=input()

for elem in S:
    if elem=="F":
        x+=dx[dir_num]
        y+=dy[dir_num]
    elif elem=="L":
        dir_num=(dir_num-1)%4
    else:
        dir_num=(dir_num+1)%4

print(x,y)