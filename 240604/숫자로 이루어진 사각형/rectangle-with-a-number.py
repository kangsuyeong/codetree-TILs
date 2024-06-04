n=int(input())


def print_rec(n):
    s=1
    for _ in range(n):
        for _ in range(n):
            if s >9:
                s=1
            print(s,end=" ")
            s+=1
        print("")


print_rec(n)