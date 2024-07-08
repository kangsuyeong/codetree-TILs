N=int(input())

class Data:
    def __init__(self,date,day,weather):
        self.date=date
        self.day=day
        self.weather=weather


ans=Data("9999-99-99","","")

for _ in range(N):
    date,day,weather=input().split()
    if weather == "Rain":
        f=Data(date,day,weather)
        if ans.date > f.date:
            ans=f

print(ans.date,ans.day,ans.weather)