n=int(input())

arr=list(map(int,input().split()))

new_arr = []
i=1
cnt=0
for elem1 in arr:
    for elem2 in arr[i:]:
        if elem1==elem2:
            cnt+=1