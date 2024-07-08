N=int(input())

class Person:
    def __init__(self,name,B,region):
        self.name=name
        self.B=B
        self.region=region
    

person =[]
for _ in range(N):
    name,B,region=input().split()
    person.append(Person(name,B,region))

index=0

for i in range(1,N):
    if person[index].name < person[i].name:
        index=i

print(f'name {person[index].name}')
print(f'addr {person[index].B}')
print(f'city {person[index].region}')