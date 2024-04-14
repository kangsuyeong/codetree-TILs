arr=input().split()

a=int(arr[0])
b=int(arr[1])

prod=1

for _ in range(b):
    prod*=a

print(prod)