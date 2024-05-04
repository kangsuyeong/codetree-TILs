n=int(input())

arr=list(map(int,input().split()))

max_val=-1
for elem1 in arr:
    if elem1>max_val:
        cnt=0
        for elem2 in arr:
            if elem1==elem2:
                cnt+=1
        
        if cnt==1:
            max_val=elem1

print(max_val)