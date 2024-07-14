x,y=0,0
dx=[0,1,0,-1]
dy=[1,0,-1,0]
dir_num=0

S=input()

for i in range(len(S)):
    if S[i]=="F":
        x+=dx[dir_num]
        y+=dy[dir_num]
    elif S[i]=="L":
        dir_num=(dir_num-1)%4
    else:
        dir_num=(dir_num+1)%4

print(x,y)