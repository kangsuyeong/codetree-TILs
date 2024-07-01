n=int(input())
arr=list(map(int,input().split()))
arr.sort()

for elem in arr:
    print(elem,end=" ")

arr2=list(reversed(arr))
print()
for elem in arr2:
    print(elem,end=" ")