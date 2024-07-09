N,K = map(int,input().split())
arr=[]
for _ in range(N+1):
    arr.append(0)

for _ in range(K):
    A,B=map(int,input().split())
    for i in range(A,B+1):
        arr[i]+=1

print(max(arr))