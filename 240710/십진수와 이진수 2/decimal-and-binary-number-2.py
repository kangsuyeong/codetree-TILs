N=input()
num=0

for digits in N:
    num=num*2 + int(digits)

num=num*17

digits=[]
while True:
    digits.append(num%2)
    num=num//2

    if num==1:
        digits.append(num)
        break;

print(*digits[::-1],sep="")