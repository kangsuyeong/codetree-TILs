#A[s] ~ A[e]를 뺀다. => 겨로가 리스트 반환
def f(A,s,e):
    temp=[]
    for i in range(len(A)):
        if s<=i<=e:
            continue
        temp.append(A[i])
    return temp

N=int(input())

A=[int(input()) for _ in range(N)]

for _ in range(2):
    s,e=map(int,input().split())
    A=f(A,s-1,e-1)

print(len(A))
print(*A, sep="\n")

# s1,e1=map(int,input().split())
# s2,e2=map(int,input().split())
# temp=[]

# for i in range(s1-1,e1):
#     arr[i]=0

# for i in range(n):
#     if arr[i]!=0:
#         temp.append(arr[i])

# arr=temp
# temp=[]

# for i in range(s2-1,e2):
#     arr[i]=0

# for i in range(len(arr)):
#     if arr[i]!=0:
#         temp.append(arr[i])

# print(len(temp))
# for elem in temp:
#     print(elem)