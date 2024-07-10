a,b=map(int,input().split())
n=input()
num=0
for digits in n:
    num=num*a+int(digits)

digits=[]

while True:
    if num<b:
        digits.append(num)
        break;
    digits.append(num%b)
    num=num//b
    
print(*digits[::-1],sep="")