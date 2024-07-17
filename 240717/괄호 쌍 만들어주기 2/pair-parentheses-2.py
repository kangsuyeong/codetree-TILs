A=input()
n=len(A)
ans=0
for i in range(n-1):
    for j in range(n-1):
        if A[i]=='(' and A[i+1]=='(' and A[j]==')' and A[j+1]==')':
            ans+=1

print(ans)