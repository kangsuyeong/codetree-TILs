class Person:
    def __init__(self,name,h,w):
        self.name=name
        self.h=h
        self.w=w

person=[]
for _ in range(5):
    name,h,w=input().split()
    person.append(Person(name,int(h),float(w)))

person.sort(key=lambda p:p.name)
print("name")
for p in person:
    print(p.name,p.h,p.w)

person.sort(key=lambda p:-p.h)
print("\nheight")
for p in person:
    print(p.name,p.h,p.w)