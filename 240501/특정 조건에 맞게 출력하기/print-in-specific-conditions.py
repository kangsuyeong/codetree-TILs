arr=list(map(int,input().split()))
new_arr=[]

for elem in arr:
    if elem==0:
        break
    elif elem%2==1:
        new_arr.append(elem+3)
    else:
        new_arr.append(elem//2)

for elem in new_arr:
    print(elem,end=" ")