import sys
n=int(input())
A=list(map(int,input().split()))

min_num=sys.maxsize

for i in range(n): #집
    S=0
    for j in range(n): #거리
        S+=A[j]*(abs(j-i))
    if S<min_num:
        min_num=S
    
print(min_num)