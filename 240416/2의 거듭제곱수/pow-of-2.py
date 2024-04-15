n=int(input())

x=0
prod=1
while True:
    prod*=2
    x+=1
    if prod==n:
        break
print(x)