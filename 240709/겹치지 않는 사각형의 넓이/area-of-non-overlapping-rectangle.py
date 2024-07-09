OFFSET=1000
# arr = [[[0] for _ in range(2005)] for _ in range(2005)]
arr = [[0]*2005 for _ in range(2005)]

for i in range(3):
    x1,y1,x2,y2 = map(lambda x:int(x) + OFFSET,input().split())
    if i==2:
       for x in range(x1,x2):
        for y in range(y1,y2):
            arr[x][y]=0
    else: 
        for x in range(x1,x2):
            for y in range(y1,y2):
                arr[x][y]=1



total=0
for row in arr:
    total+=sum(row)
print(total)