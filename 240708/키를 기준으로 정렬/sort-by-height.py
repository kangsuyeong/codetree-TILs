n=int(input())

class Person:
    def __init__(self,name,ht,wt):
        self.name = name
        self.ht = ht
        self.wt = wt
    
person = []

for _ in range(n):
    name,ht,wt=input().split()
    person.append(Person(name,int(ht),int(wt)))

person.sort(key=lambda x:x.ht)

for st in person:
    print(st.name,st.ht,st.wt)