N=int(input())

class Data:
    def __init__(self,dd,D,W):
        self.dd=dd
        self.D=D
        self.W=W

data=[]

for _ in range(N):
    dd,D,W=input().split()
    data.append(Data(dd,D,W))


cnt=0
index=0
for i in range(N):
   if data[i].W=="Rain":
    if cnt==0:
        index=i
        cnt+=1
    else :
        if data[i].dd<data[index].dd:
            index=i

print(data[index].dd,data[index].D,data[index].W)