n=int(input())
OFFSET=1000
arr = [0]*(2*OFFSET+1)
# num,D = input().split()
# num=int(num)
# print(num,D)
# current=OFFSET
# for i in range(current,current+num):
#     arr[i]+=1
#     current+=num
# print(arr[1000])

current=OFFSET
for _ in range(n):
    num,D = input().split()
    num=int(num)
    if D == "L":
        for i in range(current-1,current-num-1,-1):
            arr[i]+=1
        current-=num
    else:
        for i in range(current,current+num):
            arr[i]+=1
        current=current+num

total=0
for elem in arr:
    if elem>=2:
        total+=1
print(total)