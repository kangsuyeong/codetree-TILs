n=int(input())

satisfiy=True
for i in range(2,n):
    if n%i==0:
        satisfiy=False

if satisfiy:
    print("P")
else:
    print("C")