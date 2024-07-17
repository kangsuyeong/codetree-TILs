arr =[
    list(map(int,input().split()))
    for _ in range(19)
]

def in_range(x,y):
    return 0<=x and x<19 and 0<=y and y<19

win=0
win_x=0
win_y=0

for i in range(19):
    for j in range(19):
        #가로
        cnt=0
        for k in range(5):
            if arr[i][j]!=0 and in_range(i,j+k) and arr[i][j+k]==arr[i][j]:
                cnt+=1
            if cnt==5:
                win=arr[i][j]
                win_x=i
                win_y=j+2
                break;

        cnt=0
        for k in range(5):
            if arr[i][j]!=0 and in_range(i+k,j) and arr[i+k][j]==arr[i][j]:
                cnt+=1
            if cnt==5:
                win=arr[i][j]
                win_x=i+2
                win_y=j
                break;

        cnt=0
        for k in range(5):
            if arr[i][j]!=0 and in_range(i+k,j+k) and arr[i+k][j+k]==arr[i][j]:
                cnt+=1
            if cnt==5:
                win=arr[i][j]
                win_x=i+2
                win_y=j+2
                break;

        cnt=0
        for k in range(5):
            if arr[i][j]!=0 and in_range(i+k,j-k) and arr[i+k][j-k]==arr[i][j]:
                cnt+=1
            if cnt==5:
                win=arr[i][j]
                win_x=i+2
                win_y=j-2
                break;
print(win)
print(win_x+1,win_y+1)