n=int(input())
even_arr=[]

arr=list(map(int,input().split()))

for elem in arr:
    if elem%2==0:
        even_arr.append(elem)

for elem in even_arr:
    print(elem,end=" ")