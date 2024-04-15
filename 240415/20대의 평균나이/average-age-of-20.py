sum_val=0
cnt = 0
while True:
    n=int(input())
 
    if n<20 or n>29:
        print(f'{sum_val/cnt:.2f}')
        break
    
    sum_val+=n
    cnt+=1