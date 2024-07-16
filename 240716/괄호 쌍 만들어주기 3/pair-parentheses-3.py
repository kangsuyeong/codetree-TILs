# A=list(input())

# n=len(A)
# cnt=0
# for i in range(n):
#         for j in range(i+1,n):
#             if A[i]=='(' and A[j]==')':
#                 cnt+=1

cnt=0
answer=0
for s in input():
    if s=="(":
        cnt+=1
    else:
        answer+=cnt


print(answer)