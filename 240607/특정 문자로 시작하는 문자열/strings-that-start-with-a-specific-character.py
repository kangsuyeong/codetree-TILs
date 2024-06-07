n=int(input())

arr=[input() for _ in range(n)]

s=input()
cnt=0
sum=0
for elem in arr:

    if s == elem[0]:
        cnt+=1
        sum+=len(elem)
avg = sum / cnt
print(f'{cnt} {avg:.2f}')