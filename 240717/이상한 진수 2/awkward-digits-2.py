a=list(map(int,input()))

max_num=0
for i in range(len(a)):
    a[i]=1-a[i]
    S=0
    for digit in a:
        S=S*2 + digit
    max_num=(max(max_num,S))
    a[i]=1-a[i]

print(max_num)