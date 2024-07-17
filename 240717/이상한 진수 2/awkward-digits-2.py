a=list(map(int,input()))

max_num=0
for i in range(len(a)):
    a[i]=(a[i]+1)%2
    S=0
    for digit in a:
        S=S*2 + digit
    max_num=(max(max_num,S))
    a[i]=(a[i]+1)%2

print(max_num)