N=int(input())

class Distance:
    def __init__(self,x,y,number):
        self.x=x
        self.y=y
        self.number=number

distance=[]
for i in range(1,N+1):
    x,y=map(int,input().split())
    distance.append(Distance(x,y,i))

distance.sort(key=lambda d:abs(d.x)+abs(d.y))

for d in distance:
    print(d.number)