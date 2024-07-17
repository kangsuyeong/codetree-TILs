import sys
N=int(input()) # N개의 방

arr=[int(input()) for _ in range(N)]


min_num=sys.maxsize
#시작점 뽑기 i 시작점
for i in range(N):
    S=0
    #거리 계산
    for j in range(N):
        
        S+=arr[j]*((j-i)%5)
    min_num=min(min_num,S)
print(min_num)