arr_2D = [list(map(int,input().split())) for _ in range(2)]

for i in range(2):
    print(f'{sum(arr_2D[i])/4:.1f}',end=" ")
print("")
for j in range(4):
    sum_val=0
    for i in range(2):
        sum_val+=arr_2D[i][j]
    print(f'{sum_val/2:.1f}',end=" ")
print("")
sum_val=0
for i in range(2):
    for j in range(4):
        sum_val+=arr_2D[i][j]

print(f'{sum_val/8:.1f}')