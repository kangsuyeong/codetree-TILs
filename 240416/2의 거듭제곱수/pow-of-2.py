n=int(input())

cnt=0
while True:
    n//=2
    cnt+=1
    if(n==1):
        break
    

print(cnt)