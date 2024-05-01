n=int(input())
even_arr=[]

arr=list(map(int,input().split()))

for elem in arr:
    if elem%2==0:
        even_arr.append(elem)

for i in range(len(even_arr)):
    print(even_arr[i],end=" ")