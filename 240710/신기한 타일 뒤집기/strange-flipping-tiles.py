n=int(input())
OFFSET = n*100

arr=[0]*(2*OFFSET+1)

current=OFFSET
for _ in range(n):
    num,D = input().split()
    num=int(num)
    if D=='R':
        for i in range(current,current+num):
            arr[i]=2
        current=current+num-1
    else:
        for i in range(current,current-num,-1):
            arr[i]=1
        current=current-num+1

white_cnt=0
black_cnt=0

for elem in arr:
    if elem==2:
        black_cnt+=1
    elif elem==1:
        white_cnt+=1

print(white_cnt,black_cnt)