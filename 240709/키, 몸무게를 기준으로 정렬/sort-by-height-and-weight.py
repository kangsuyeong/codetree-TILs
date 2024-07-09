N=int(input())

class Person:
    def __init__(self,name,h,w):
        self.name=name
        self.h=h
        self.w=w

person=[]
for _ in range(N):
    name,h,w=input().split()
    person.append(Person(name,int(h),int(w)))

person.sort(key=lambda p:(p.h,-p.w))

for p in person:
    print(p.name,p.h,p.w)