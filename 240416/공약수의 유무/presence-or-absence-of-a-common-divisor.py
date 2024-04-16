arr=input().split()

a=int(arr[0])
b=int(arr[1])

satisfiy=False

for i in range(a,b+1):
    if 1920%i==0 and 2880%i==0:
        satisfiy=True

if satisfiy:
    print(1)
else:
    print(0)