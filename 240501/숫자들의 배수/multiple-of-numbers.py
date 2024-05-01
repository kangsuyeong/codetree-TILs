n=int(input())
arr=[]
cnt=1
cnt_5=0
while 1:
    arr.append(n*cnt)
    if arr[cnt-1]%5==0:
        cnt_5+=1
    print(arr[cnt-1],end=" ")

    if cnt_5==2:
        break
    cnt+=1