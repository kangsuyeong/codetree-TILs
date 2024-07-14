N=int(input())

D = ["E","W","S","N"]
x,y=0,0
dx=[1,-1,0,0]
dy=[0,0,-1,1]


for _ in range(N):
    input_D,input_num=input().split()
    input_num=int(input_num)
    x = x+dx[D.index(input_D)]*input_num
    y = y+dy[D.index(input_D)]*input_num

print(x,y)