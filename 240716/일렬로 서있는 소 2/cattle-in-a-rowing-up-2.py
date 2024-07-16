N=int(input())

A=list(map(int,input().split()))
ans=0
for i in range(len(A)):
    for j in range(i+1,len(A)):
        for k in range(j+1,len(A)):
            if A[i]<=A[j] and A[j]<=A[k]:
                ans+=1

print(ans)