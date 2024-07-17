arr =[
    list(map(int,input().split()))
    for _ in range(19)
]

def in_range(x,y):
    return 0<=x and x<19 and 0<=y and y<19

win=0
win_x=0
win_y=0

dx,dy=[0,1,1,1],[1,1,0,-1]

for i in range(19):
    for j in range(19):


        for k in range(4):
            cnt=1
            for l in range(1,5):
                if arr[i][j]!=0 and in_range(i+dx[k]*l,j+dy[k]*l) and arr[i+dx[k]*l][j+dy[k]*l]==arr[i][j]:
                    cnt+=1
                if cnt==5:
                    win=arr[i][j]
                    win_x=i+dx[k]*2
                    win_y=j+dy[k]*2
                

print(win)
if win!=0:
    print(win_x+1,win_y+1)