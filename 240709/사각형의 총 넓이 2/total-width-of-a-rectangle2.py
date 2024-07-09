N=int(input())
arr=[
    [0 for _ in range(205)]
    for _ in range(205)
    ]

OFFSET=100

for _ in range(N):
    x1,y1,x2,y2 = map(lambda x: int(x)+OFFSET,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            arr[i][j]=1

area=0
for row in arr:
    area +=sum(row)

print(area)