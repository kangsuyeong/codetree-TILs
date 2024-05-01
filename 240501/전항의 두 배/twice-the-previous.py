a1,a2=tuple(map(int,input().split()))
arr=[]

arr.append(a1)
arr.append(a2)

for i in range(2,10):
    arr.append(arr[i-1]+2*arr[i-2])

for elem in arr:
    print(elem,end=" ")