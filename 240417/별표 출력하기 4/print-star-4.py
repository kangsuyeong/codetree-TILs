n=int(input())

for i in range(n):
    for _ in range(n-i):
        print("*",end=" ")
    print("")

for i in range(n-1):
    for _ in range(i+2):
        print("*",end=" ")
    print("")