arr=input().split()

a=int(arr[0])
b=int(arr[1])
c=int(arr[2])

check = False

for i in range(a,b+1):
    if(c%i ==0):
        check = True

if check==True:
    print("YES")
else:
    print("NO")