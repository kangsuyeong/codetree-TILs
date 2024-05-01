arr=[]
p1,p2=tuple(map(int,input().split()))

arr.append(p1)
arr.append(p2)

for i in range(2,10):
    arr.append((arr[i-2]+arr[i-1])%10)

for elem in arr:
    print(elem,end=" ")