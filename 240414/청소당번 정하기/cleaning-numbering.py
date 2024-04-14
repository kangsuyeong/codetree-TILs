n=int(input())

cntB = 0
cntR =0
cntH =0
for i in range(1,n+1):
    if i%12==0:
        cntH+=1
    elif i%3==0:
        cntB+=1
    elif i%2==0:
        cntR+=1

print(cntR,cntB,cntH)