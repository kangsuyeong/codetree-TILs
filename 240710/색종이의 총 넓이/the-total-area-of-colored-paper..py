N = int(input())
OFFSET=100

arr=[[0]*200 for _ in range(200)]


for _ in range(N):
    x,y=map(lambda x:int(x)+OFFSET,input().split())
    for i in range(x,x+8):
        for j in range(y,y+8):
            arr[i][j]=1
    total=0

total=0
for row in arr:
    total+=sum(row)

print(total)