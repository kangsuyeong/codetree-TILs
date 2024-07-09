N=int(input())

class Student:
    def __init__(self,h,w,number):
        self.h=h
        self.w=w
        self.number=number

student=[]
for i in range(1,N+1):
    h,w=map(int,input().split())
    student.append(Student(h,w,i))

student.sort(key=lambda st:(st.h,-st.w))

for st in student:
    print(st.h,st.w,st.number)