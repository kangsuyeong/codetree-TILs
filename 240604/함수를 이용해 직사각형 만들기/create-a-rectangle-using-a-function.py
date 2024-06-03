n,m=tuple(map(int,input().split()))

def print_rect(col_num,row_num):
    for _ in range(col_num):
        print("1"*row_num)

print_rect(n,m)