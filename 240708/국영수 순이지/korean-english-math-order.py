N=int(input())

class Student:
    def __init__(self,name,kor,eng,math):
        self.name=name
        self.kor=kor
        self.eng=eng
        self.math=math


studnet = []
for _ in range(N):
    name,kor,eng,math = input().split()
    studnet.append(Student(name,int(kor),int(eng),int(math)))

studnet.sort(key=lambda st:(-st.kor,-st.eng,-st.math))

for st in studnet:
    print(st.name,st.kor,st.eng,st.math)