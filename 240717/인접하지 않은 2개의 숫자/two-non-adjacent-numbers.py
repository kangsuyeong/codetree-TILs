n=int(input())

arr = list(map(int,input().split()))

max_num=0
for i in range(n-2):
    for j in range(i+2,n):
        max_num=max(max_num,arr[i]+arr[j])

print(max_num)