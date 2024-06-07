n=int(input())

def fun(n):
    sum_n=0
    for i in range(1,n+1):
        sum_n+=i
    
    return sum_n//10

total = fun(n)

print(total)