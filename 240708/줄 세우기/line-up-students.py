N = int(input())

class Student:
    def __init__(self,h,w,number):
        self.h=h
        self.w=w
        self.number=number

students=[]
for i in range(N):
    h,w = map(int,input().split())
    students.append(Student(h,w,i+1))

students.sort(key=lambda st:(-st.h,-st.w,st.number))

for st in students:
    print(st.h,st.w,st.number)