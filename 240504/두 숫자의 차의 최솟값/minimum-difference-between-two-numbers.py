n=int(input())

num = list(map(int,input().split()))

diff_min=100
for i in range(n):
    for j in range(i+1,n):
        diff=num[j]-num[i]
        if diff_min>diff:
            diff_min=diff

print(diff_min)