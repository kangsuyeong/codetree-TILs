n=int(input())
arr=list(map(int,input().split()))

if arr[0]>=arr[1]:
    max1,max2=arr[0],arr[1]
else:
    max1,max2=arr[1],arr[0]

for elem in arr[2:]:
    if elem>max1:
        max1,max2=elem,max1
    elif elem>max2:
        max2=elem

print(max1,max2)