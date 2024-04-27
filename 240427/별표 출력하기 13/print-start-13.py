n=int(input())

for i in range(1,2*n+1):
    if i%2==0:
        for _ in range((i+1)//2):
            print("*",end=" ")
    else:
        for _ in range(n-i//2):
            print("*",end=" ")
    print()