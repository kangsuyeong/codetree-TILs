arr=list(map(int,input().split()))

sum_val=0
cnt = 0
for i in range(10):
    if arr[i]<250:
        sum_val+=arr[i]
    else :
        break;
    cnt+=1

print(f'{sum_val} {sum_val/cnt:.1f}')