sum_val=0
cnt=0
for _ in range(10):
    a=int(input())
    if a>=0 and a<=200:
        sum_val+=a
        cnt+=1

print(f'{sum_val} {sum_val/cnt:.1f}')