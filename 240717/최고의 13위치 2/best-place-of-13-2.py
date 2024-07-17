N=int(input())
arr=[
    list(map(int,input().split()))
    for _ in range(N)
]

def in_range(y):
    return 0<=y and y<N
box1=0
box2=0
max_num=0
for i in range(N):
    for j in range(N-2):
        for k in range(i,N):
            for l in range(N-2):
                if i==k and (l-j)<3:
                    continue
                ans=0
                ans+=arr[i][j]+arr[i][j+1]+arr[i][j+2]
                ans+=arr[k][l]+arr[k][l+1]+arr[k][l+2]
                max_num=max(max_num,ans)
print(max_num)