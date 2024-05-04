n=int(input())

price = list(map(int,input().split()))

profit=0

for i in range(n):
    for j in range(i+1,n):
        if price[i]<price[j]:
            if profit<price[j]-price[i]:
                profit=price[j]-price[i]

print(profit)