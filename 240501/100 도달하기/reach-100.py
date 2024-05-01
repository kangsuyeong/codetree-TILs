n=int(input())
arr=[1,n]

i=2
while 1:
    arr.append(arr[i-2]+arr[i-1])
    if arr[i]>100:
        break;
    i+=1

for elem in arr:
    print(elem,end=" ")