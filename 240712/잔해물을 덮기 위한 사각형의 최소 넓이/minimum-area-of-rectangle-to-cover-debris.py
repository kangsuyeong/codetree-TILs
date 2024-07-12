OFFSET = 1000

arr=[[0]*(2*OFFSET+1) for _ in range(2*OFFSET+1)]
x1,y1,x2,y2= map(lambda x:int(x)+OFFSET,input().split())
xx1,yy1,xx2,yy2= map(lambda x:int(x)+OFFSET,input().split())

x_min=OFFSET*2
x_max=0
y_min=OFFSET*2
y_max=0

for i in range(x1,x2+1):
    for j in range(y1,y2+1):
        arr[i][j]=1

for i in range(xx1,xx2+1):
    for j in range(yy1,yy2+1):
        arr[i][j]=2

for i in range(x1,x2+1):
    for j in range(y1,y2+1):
        if arr[i][j]==1:
            x_min=min(x_min,i)
            x_max=max(x_max,i)
            y_min=min(y_min,j)
            y_max=max(y_max,j)
if x_max-x_min<0 or y_max-y_min<0:
    print(0)
else:
    print((x_max-x_min)*(y_max-y_min))