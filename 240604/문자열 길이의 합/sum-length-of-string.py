n=int(input())

arr=[input() for _ in range(n)]
total=0
cnt=0
for elem in arr:
    total+=len(elem)
    if elem[0]=="a":
        cnt+=1

print(total,cnt)