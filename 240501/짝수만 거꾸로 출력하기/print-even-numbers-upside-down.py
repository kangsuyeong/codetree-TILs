n=int(input())
new_arr=[]
arr=list(map(int,input().split()))

for elem in arr:
    if elem%2==0:
        new_arr.append(elem)

for i in range(len(new_arr)-1,-1,-1):
    print(new_arr[i],end=" ")