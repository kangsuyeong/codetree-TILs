n=int(input())

arr=[int(input()) for _ in range(n)]

s1,e1=map(int,input().split())
s2,e2=map(int,input().split())
temp=[]

for i in range(s1-1,e1):
    arr[i]=0

for i in range(n):
    if arr[i]!=0:
        temp.append(arr[i])

arr=temp
temp=[]

for i in range(s2-1,e2):
    arr[i]=0

for i in range(len(arr)):
    if arr[i]!=0:
        temp.append(arr[i])

print(len(temp))
for elem in temp:
    print(elem)