# N*N크기
N=int(input())

# 입력받기
arr =[
    list(map(int,input().split()))
    for _ in range(N)
]
max_num=0
for i in range(N-2):
    for j in range(N-2):
        sum_num=0
        for k in range(3):
            for l in range(3):
                sum_num+=arr[i+k][j+l]
        max_num=max(max_num,sum_num)

print(max_num)