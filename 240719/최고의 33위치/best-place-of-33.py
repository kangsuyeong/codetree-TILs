N=int(input())

arr=[
    list(map(int,input().split()))
    for _ in range(N)
]

max_num=0
for i in range(N-2):
    for j in range(N-2):
        s=0
        for k in range(3):
           for l in range(3):
                s+=arr[i+k][j+l]
        max_num=max(max_num,s)

print(max_num)