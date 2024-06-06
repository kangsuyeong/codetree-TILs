n,m=map(int,input().split())

def cal_num(a,b):
    arr_a=[]
    arr_b=[]
    arr_c=[]
    for i in range(1,a):
        if a%i ==0:
            arr_a.append(i)
    for i in range(1,b):
        if b%i ==0:
            arr_b.append(i)
    for item in arr_a:
        if item not in arr_b:
            arr_c.append(item)

    for item in arr_b:
        if item not in arr_a:
            arr_c.append(item)
    final = 1
    for item in arr_c:
        final *=item
    
    print(final)

cal_num(n,m)