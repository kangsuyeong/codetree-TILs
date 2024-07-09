n=int(input())
digits =[]
while True:
    digits.append(n%2)
    n=n//2

    if n==0:
        break;

print(*digits[::-1],sep="")