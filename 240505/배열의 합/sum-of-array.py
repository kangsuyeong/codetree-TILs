arr_2D = [list(map(int,input().split())) for _ in range(4)]

for i in range(4):
    sum=0
    for j in range(4):
        sum+=arr_2D[i][j]
    print(sum)