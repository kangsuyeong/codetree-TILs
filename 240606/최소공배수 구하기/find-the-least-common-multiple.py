n,m=map(int,input().split())

def cal_num(a,b):
    for i in range(max(a,b),a*b+1):
        if i%a == 0 and i%b ==0:
            print(i)
            break;

cal_num(n,m)