n,m=map(int,input().split())

def num_cal(n,m):
    for i in range(min(n,m),0,-1):
        same_num=0
        if n % i ==0 and m%i==0:
            same_num=i
            break;
    print(same_num)
        
    
num_cal(n,m)