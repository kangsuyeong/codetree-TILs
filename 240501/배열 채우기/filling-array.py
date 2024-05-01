new_arr=[]
arr=list(map(int,input().split()))



cnt = len(arr)
for i in range(cnt):
    if arr[i]==0:
        cnt=i
    else :
        new_arr.append(arr[i])

for i in range(cnt-1,-1,-1):
    print(new_arr[i],end=" ")