arr_2D = [list(map(int,input().split())) for _ in range(4)]

sum_val=0

for i in range(4):
    for j in range(i+1):
        sum_val+=arr_2D[i][j]

print(sum_val)