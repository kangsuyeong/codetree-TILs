n=int(input())

for i in range(1,2*n+1):
    if i%2==1:
        for _ in range(i):
            print("*",end=" ")

    if i%2==0:
        for _ in range(n-i+1):
            print("*",end=" ")
    print("")