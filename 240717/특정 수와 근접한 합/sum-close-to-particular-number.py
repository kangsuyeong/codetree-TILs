import sys
N,S=map(int,input().split())

arr=list(map(int,input().split()))
s1=sum(arr)

min_num=sys.maxsize

s2=0
for i in range(N):
    for j in range(i,N):
        s2=arr[i]+arr[j]
        min_num=min(min_num,abs(S-(s1-s2)))

print(min_num)