arr=input().split()

a=int(arr[0])
b=int(arr[1])

print(f'{a//b}.',end="")

for _ in range(20):
    a%=b
    a*=10
    print(a//b,end="")