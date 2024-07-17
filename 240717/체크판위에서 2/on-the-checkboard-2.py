R,C=map(int,input().split())

arr=[
    list(input().split())
    for _ in range(R)
]

jump1=0
jump2=0

cnt=0
for i in range(1,R):
    for j in range(1,C):
        if arr[0][0]!=arr[i][j]:
            for k in range(i+1,R-1):
                for l in range(j+1,C-1):
                    if arr[i][j]!=arr[k][l]:
                        cnt+=1

print(cnt)