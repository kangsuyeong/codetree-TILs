import sys
n=int(input())

arr=list(map(int,input().split()))

idx=n
while 1:
    max_val = -sys.maxsize
    for i in range(idx): #1-4까지 비교
        if arr[i]>max_val:
            max_val=arr[i]
            idx=i #idx=2
    print(idx+1,end=" ")
    if idx==0:
        break;