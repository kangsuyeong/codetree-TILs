s=input()
n=int(input())

leng=len(s)
cnt=0

for i in range(leng-1,-1,-1):
    if cnt>=n:
        break;
    cnt+=1
    print(s[i],end="")