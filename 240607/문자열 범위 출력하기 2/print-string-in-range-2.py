s=input()
n=int(input())

leng=len(s)

for i in range(leng-1,leng-1-n,-1):
    print(s[i],end="")