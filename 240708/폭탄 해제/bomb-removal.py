class Bomb:
    def __init__(self,code,color,second):
        self.code = code
        self.color = color
        self.second = second
    

code ,color,second = input().split()

bomb1= Bomb(code,color,int(second))
print(f'code : {bomb1.code}')
print(f'color : {bomb1.color}')
print(f'second : {bomb1.second}')