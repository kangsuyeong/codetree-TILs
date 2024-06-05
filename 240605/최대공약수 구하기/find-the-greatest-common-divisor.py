n,m=map(int,input().split())

def num_cal(n,m):
    min_num = min(n,m)
    max_num = max(n,m)

    same_num=0
    for i in range(min_num,0,-1):
        if max_num % i ==0 and min_num%i==0:
            same_num=i
            break;
    print(same_num)
        
    
num_cal(n,m)