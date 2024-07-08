class Spy:
    def __init__(self,name,score):
        self.name = name
        self.score = score


spy = []
index=0
for _ in range(5):
    name,score = input().split()
    spy.append(Spy(name,int(score)))

for i in range(1,5):
    if spy[index].score > spy[i].score:
        index = i

print(spy[index].name,spy[index].score)