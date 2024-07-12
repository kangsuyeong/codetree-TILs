n=int(input())
OFFSET=100
arr=[[0]*(2*OFFSET+1) for _ in range(2*OFFSET+1)]

for i in range(n):
    x1,y1,x2,y2=map(lambda x:int(x)+OFFSET,input().split())
    for j in range(x1,x2):
        for k in range(y1,y2):
            if i%2==0:
                arr[j][k]=1
            else :
                arr[j][k]=2
total=0
for row in arr:
    for elem in row:
        if elem==2:
            total+=1
print(total)