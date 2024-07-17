N=int(input())
arr=[
    list(map(int,input().split()))
    for _ in range(N)
]

def in_range(y):
    return 0<=y and y<N
box1=0
box2=0

for i in range(N):
    for j in range(N-2):
        ans=0
        ans+=arr[i][j]+arr[i][j+1]+arr[i][j+2]
        for k in range(N):
            if i==k:
                for l in range(j+2,N-2):
                    if in_range(l) and in_range(l+1) and in_range(l+2):
                        ans+=arr[k][l]+arr[k][l+1]+arr[k][l+2]
            else :
                for l in range(N-2):
                    ans+=arr[k][l]+arr[k][l+1]+arr[k][l+2]

print(ans)