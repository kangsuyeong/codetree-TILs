arr= list(map(int,input().split()))

max_val=0
min_val=1000

for elem in arr:
    if elem>500:
        if min_val>elem:
            min_val=elem
    else :
        if max_val<elem:
            max_val=elem

print(max_val,min_val)