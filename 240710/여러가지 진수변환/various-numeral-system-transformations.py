N,B=map(int,input().split())

digits=[]

while True:
    digits.append(N%B)
    N= N//B
    if N==0:
        break;

print(*digits[::-1],sep="")