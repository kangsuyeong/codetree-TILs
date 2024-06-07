n=int(input())

arr=[input() for _ in range(n)]

s=input()
cnt=0
sum=0
for elem in arr:
    sum+=len(elem)
    if s == elem[0]:
        cnt+=1
avg = sum // len(arr)
print(f'{cnt} {avg:.2f}')