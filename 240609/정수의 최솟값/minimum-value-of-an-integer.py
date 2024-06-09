def cal(a,b,c):
    return min(a,b,c)

a,b,c=map(int,input().split())

min_num = cal(a,b,c)
print(min_num)