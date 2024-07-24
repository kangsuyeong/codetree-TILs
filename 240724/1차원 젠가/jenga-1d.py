n=int(input())
arr=[int(input()) for _ in range(n)]





# 2번 하기
for _ in range(2):
    temp=[]
    s,e=map(int,input().split())
    for i in range(len(arr)):
        if s-1<=i<=e-1:
            continue
        temp.append(arr[i])
    # arr초기화
    arr=temp
print(len(arr))
for elem in arr:
    print(elem)