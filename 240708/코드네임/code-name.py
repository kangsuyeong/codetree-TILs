class Spy:
    def __init__(self,name,score):
        self.name = name
        self.score = score


spy = []
index=0
min_score = 100
for i in range(5):
    name,score = input().split()
    spy.append(Spy(name,int(score)))
    if min_score > min(min_score,int(score)):
        min_score = int(score)
        index = i

print(spy[index].name,spy[index].score)